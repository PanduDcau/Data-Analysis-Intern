import argparse
import DataCleaning
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, log_loss
import xgboost as xgb
import matplotlib as mpl
import mlflow
import mlflow.xgboost

mpl.use("Agg")


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

    # import from dataset_cleaning.py
    out = DataCleaning.Dataclean()
    data, X_train, X_test, y_train, y_test = out.cleandata()

    import configparser
    config = configparser.ConfigParser()
    config.read(r'config.ini')
    type = config.get('type', 'input_path_3')
    response = config.get('response', 'input_path_2')
    y = data[response]

    if type == "Classification":
        # enable auto logging
        mlflow.xgboost.autolog()

        dtrain = xgb.DMatrix(X_train, label=y_train)
        dtest = xgb.DMatrix(X_test, label=y_test)

        with mlflow.start_run():
            leve = y.value_counts().count()
            # train model
            params = {
                "objective": "multi:softprob",
                "num_class": leve,
                "learning_rate": args.learning_rate,
                "eval_metric": "mlogloss",
                "colsample_bytree": args.colsample_bytree,
                "subsample": args.subsample,
                "seed": 42,
            }
            model = xgb.train(params, dtrain, evals=[(dtrain, "train")])

            # evaluate model
            y_proba = model.predict(dtest)
            y_pred = y_proba.argmax(axis=1)
            loss = log_loss(y_test, y_proba)
            acc = accuracy_score(y_test, y_pred)

            # log metrics
            mlflow.log_metrics({"log_loss": loss, "accuracy": acc})

    else:
        print("Cannot run the selected model")


if __name__ == "__main__":
    main()
    print("Model Created")
