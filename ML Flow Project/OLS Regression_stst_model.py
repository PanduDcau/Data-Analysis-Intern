from sklearn.model_selection import train_test_split
import argparse
import mlflow
import statsmodels.api as sm
import mlflow.statsmodels
from sklearn.metrics import mean_squared_error
import DataCleaning
import configparser


def parse_args():
    parser = argparse.ArgumentParser(description="Statsmodels example")
    parser.add_argument(
        "--inverse-method",
        type=str,
        default="pinv",
        help="Can be 'pinv', or 'qr'. 'pinv' uses the Moore-Penrose pseudoinverse "
             "to solve the least squares problem. 'qr' uses the QR factorization. "
             "(default: 'pinv')",
    )
    return parser.parse_args()


config = configparser.ConfigParser()
config.read(r'config.ini')
type = config.get('type', 'input_path_3')

if type == "Regression":
    def main():
        # parse command-line arguments
        args = parse_args()

        # prepare train and test data
        # Ordinary Least Squares (OLS)
        out = DataCleaning.Dataclean()
        data, X_train, X_test, y_train, y_test = out.cleandata()

        # enable auto logging
        mlflow.statsmodels.autolog()

        with mlflow.start_run():
            ols = sm.OLS(y_train, X_train)
            model = ols.fit(method=args.inverse_method)

            # evaluate model
            y_pred = model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)

            # log metrics
            mlflow.log_metrics({"mse": mse})

if __name__ == "__main__":
    main()
    print("Model Created ")
else:
    print("Cannot run the selected model")
