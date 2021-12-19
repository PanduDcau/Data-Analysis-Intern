from sklearn.linear_model import LogisticRegression
import mlflow.sklearn
from sklearn.model_selection import train_test_split
import DataCleaning

if __name__ == "__main__":
    # import from dataset_cleaning.py
    out = DataCleaning.Dataclean()
    data, X_train, X_test, y_train, y_test = out.cleandata()

    import configparser

    config = configparser.ConfigParser()
    config.read(r'config.ini')
    type = config.get('type', 'input_path_3')

    if type == "Classification":
        lr = LogisticRegression(max_iter=10)
        lr.fit(X_train, y_train)
        predicted_qualities = lr.predict(X_test)
        score = lr.score(X_test, predicted_qualities)
        print("Score: %s" % score)
        mlflow.log_metric("score", score)
        mlflow.sklearn.log_model(lr, "model")
        print("Model saved in run %s" % mlflow.active_run().info.run_uuid)


    else:
        print("Cannot run the selected model")
