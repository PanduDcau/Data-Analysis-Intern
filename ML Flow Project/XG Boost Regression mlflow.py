import argparse
import DataCleaning
import numpy as np
import xgboost as xgb
import matplotlib as mpl
import mlflow
import mlflow.xgboost
import configparser
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

mpl.use("Agg")

# Read the configuration file


config = configparser.ConfigParser()
config.read(r'config.ini')
type = config.get('type', 'input_path_3')


def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2


if type == "Regression":
    def parse_args():
        parser = argparse.ArgumentParser(description="XGBoost example")
        parser.add_argument(
            "--learning-rate",
            type=float,
            default=0.3,
            help="learning rate to update step size at each boosting step (default: 0.3)",
        )
        parser.add_argument(
            "--colsample-bytree",
            type=float,
            default=1.0,
            help="subsample ratio of columns when constructing each tree (default: 1.0)",
        )
        parser.add_argument(
            "--subsample",
            type=float,
            default=1.0,
            help="subsample ratio of the training instances (default: 1.0)",
        )
        return parser.parse_args()


    def main():
        # parse command-line arguments
        args = parse_args()

        # import from DataCleaning.py
        out = DataCleaning.Dataclean()
        data, X_train, X_test, y_train, y_test = out.cleandata()

        # enable auto logging
        mlflow.xgboost.autolog()

        dtrain = xgb.DMatrix(X_train, label=y_train)
        dtest = xgb.DMatrix(X_test, label=y_test)

        with mlflow.start_run():
            # train model
            params = {
                "learning_rate": args.learning_rate,
                "colsample_bytree": args.colsample_bytree,
                "subsample": args.subsample,
                "seed": 42,
            }
            model = xgb.train(params, dtrain, evals=[(dtrain, "train")])

            # evaluate model
            predicted_qualities = model.predict(dtest)

            (rmse, mae, r2) = eval_metrics(y_test, predicted_qualities)

            print("  RMSE: %s" % rmse)
            print("  MAE: %s" % mae)
            print("  R2: %s" % r2)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)


    if __name__ == "__main__":
        main()

else:
    print("This is an Regression Model")
