import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from urllib.parse import urlparse
import DataCleaning
import mlflow
from sklearn.metrics import mean_squared_error, mean_absolute_error
from urllib.parse import urlparse
import DataCleaning
import mlflow
import logging

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)


def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    return rmse, mae


if __name__ == "__main__":
    out = DataCleaning.Dataclean()
    data, X_train, X_test, y_train, y_test = out.cleandata()
    import configparser

    config = configparser.ConfigParser()
    config.read(r'config.ini')
    type = config.get('type', 'input_path_3')

    if type == "Regression":
        with mlflow.start_run():
            rf = RandomForestRegressor(max_features='sqrt', n_estimators=200, random_state=42)
            rf.fit(X_train, y_train)
            predicted_qualities = rf.predict(X_test)

            (rmse, mae) = eval_metrics(y_test, predicted_qualities)

            print("  RMSE: %s" % rmse)
            print("  MAE: %s" % mae)

            mlflow.log_metric("rmse", rmse)

            mlflow.log_metric("mae", mae)

            tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

    else:
        print("Cannot run the selected model")
