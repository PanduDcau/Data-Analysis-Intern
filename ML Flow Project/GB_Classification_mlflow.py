import argparse
from sklearn.metrics import accuracy_score, log_loss
import lightgbm as lgb
import matplotlib as mpl
import DataCleaning
import mlflow
import mlflow.lightgbm
import mlflow.sklearn

# Read the configuration file
import configparser
config = configparser.ConfigParser()
config.read(r'config.ini')
type = config.get('type', 'input_path_3')
response = config.get('response', 'input_path_2')

mpl.use("Agg")

if type == "Classification":
    def parse_args():
        parser = argparse.ArgumentParser(description="LightGBM example")
        parser.add_argument(
            "--learning-rate",
            type=float,
            default=0.1,
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
        y = data[response]
        # enable auto logging
        mlflow.lightgbm.autolog()

        train_set = lgb.Dataset(X_train, label=y_train)

        with mlflow.start_run():
            leve = y.value_counts().count()
            # train model
            params = {
                "objective": "multiclass",
                "num_class": leve,
                "learning_rate": args.learning_rate,
                "metric": "multi_logloss",
                "colsample_bytree": args.colsample_bytree,
                "subsample": args.subsample,
                "seed": 42,
            }
            model = lgb.train(
                params, train_set, num_boost_round=10, valid_sets=[train_set], valid_names=["train"]
            )

            # evaluate model
            y_proba = model.predict(X_test)
            y_pred = y_proba.argmax(axis=1)
            loss = log_loss(y_test, y_proba)
            acc = accuracy_score(y_test, y_pred)

            # log metrics
            mlflow.log_metrics({"log_loss": loss, "accuracy": acc})


    if __name__ == "__main__":
        main()
        print("Model saved")

else:
    print("This is a classification Model")