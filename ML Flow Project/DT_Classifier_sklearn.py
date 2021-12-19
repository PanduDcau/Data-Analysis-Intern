from sklearn.tree import DecisionTreeClassifier, plot_tree, export_graphviz
from sklearn.metrics import accuracy_score
import DataCleaning
import mlflow.sklearn

# Fitting a classifier and predicting on test
dt_params = {'max_depth': 5, 'max_features': 'sqrt', 'min_samples_split': 6}

if __name__ == "__main__":
    # import from dataset_cleaning.py
    out = DataCleaning.Dataclean()
    data, X_train, X_test, y_train, y_test = out.cleandata()

    import configparser

    config = configparser.ConfigParser()
    config.read(r'config.ini')
    type = config.get('type', 'input_path_3')

    if type == "Classification":
        dt = DecisionTreeClassifier(**dt_params)
        dt.fit(X_train, y_train)
        y_pred = dt.predict(X_test)
        acc = accuracy_score(y_test, y_pred).round(3)
        print("Accuracy: %s" % acc)
        mlflow.log_metric("Accuracy", acc)
        mlflow.sklearn.log_model(dt, "model")
        print("Model saved in run %s" % mlflow.active_run().info.run_uuid)


    else:
        print("Cannot run the selected model")
