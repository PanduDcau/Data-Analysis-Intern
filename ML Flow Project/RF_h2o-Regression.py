import h2o
from h2o.estimators.random_forest import H2ORandomForestEstimator
import DataCleaning
import mlflow
import mlflow.h2o
import configparser

h2o.init()

# import from dataset_cleaning.py
out = DataCleaning.Dataclean()
data, X_train, X_test, y_train, y_test = out.cleandata()
hf = h2o.H2OFrame(data)
train, test = hf.split_frame(ratios=[.8])

config = configparser.ConfigParser()
config.read(r'config.ini')
response = config.get('response', 'input_path_2')
type = config.get('type', 'input_path_3')

if type == "Regression":
    def train_random_forest(ntrees):
        with mlflow.start_run():
            rf = H2ORandomForestEstimator(ntrees=ntrees)
            train_cols = [n for n in train.col_names if n != response]
            rf.train(train_cols, response, training_frame=train, validation_frame=test)

            mlflow.log_param("ntrees", ntrees)

            mlflow.log_metric("rmse", rf.rmse())
            mlflow.log_metric("r2", rf.r2())
            mlflow.log_metric("mae", rf.mae())

            mlflow.h2o.log_model(rf, "model")


    if __name__ == "__main__":
        for ntrees in [10, 20, 50, 100, 200]:
            train_random_forest(ntrees)

else:
    print("Cannot run the selected model")
