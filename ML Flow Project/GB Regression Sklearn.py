import argparse
import warnings
import configparser
import matplotlib.pyplot as plt
import mlflow
import numpy as np
import pandas as pd
import seaborn as sns
from mlflow.models.signature import infer_signature
from sklearn import tree
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.inspection import permutation_importance
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold, cross_val_score, train_test_split
import DataCleaning

plt.style.use("fivethirtyeight")
warnings.filterwarnings('ignore')
np.random.seed(42)

# Evaluation Metrics
def rmse(y, y_pred):
    return np.sqrt(mean_squared_error(y, y_pred))


def rmse_score(y, y_pred):
    score = rmse(y, y_pred)
    return score


# Cross-validation RMSLE score
def rmsle_cv(model, X_train, y_train):
    kf = KFold(n_splits=3, shuffle=True, random_state=42).get_n_splits(X_train.values)
    # Evaluate a score by cross-validation
    rmse = np.sqrt(-cross_val_score(model, X_train.values, y_train, scoring="neg_mean_squared_error", cv=kf))
    return rmse


def rmse_cv_score(model, X_train, y_train):
    score = rmsle_cv(model, X_train, y_train)
    return score


# Feature Importance
def model_feature_importance(model):
    feature_importance = pd.DataFrame(
        model.feature_importances_,
        index=X_train.columns,
        columns=["Importance"],
    )

    # sort by importance
    feature_importance.sort_values(by="Importance", ascending=False, inplace=True)

    # plot
    plt.figure(figsize=(12, 8))
    sns.barplot(
        data=feature_importance.reset_index(),
        y="index",
        x="Importance",
    ).set_title("Feature Importance")
    # save image
    plt.savefig(f"Model_Artifacts/feature_importance.png", bbox_inches='tight')


def model_permutation_importance(model):
    p_importance = permutation_importance(model, X_test, y_test, random_state=42, n_jobs=-1)

    # sort by importance
    sorted_idx = p_importance.importances_mean.argsort()[::-1]
    p_importance = pd.DataFrame(
        data=p_importance.importances[sorted_idx].T,
        columns=X_train.columns[sorted_idx]
    )

    # plot
    plt.figure(figsize=(12, 8))
    sns.barplot(
        data=p_importance,
        orient="h"
    ).set_title("Permutation Importance")

    # save image
    plt.savefig(f"Model_Artifacts/permutation_importance.png", bbox_inches="tight")


def model_tree_visualization(model):
    # generate visualization
    tree_dot_data = tree.export_graphviz(
        decision_tree=model.estimators_[0, 0],  # Get the first tree,
        label="all",
        feature_names=X_train.columns,
        filled=True,
        rounded=True,
        proportion=True,
        impurity=False,
        precision=1,
    )

    # save image
    #graph_from_dot_data(tree_dot_data).write_png(f"{model_artifacts_dir}/Decision_Tree_Visualization.png")


# Read the data csv file (make sure you're running this from the root of MLflow!)

# load input data into pandas dataframe
#data = pd.read_csv('abalone.csv')

# Prepare training and test data sets
out = DataCleaning.Dataclean()
data,X_train, X_test, y_train, y_test = out.cleandata()


config = configparser.ConfigParser()
config.read(r'config.ini')
type = config.get('type', 'input_path_3')

if type == "Regression":

    # main entry point
    if __name__ == "__main__":
        # parse run parameters
        parser = argparse.ArgumentParser()
        parser.add_argument('--learning_rate', type=float, default=0.1)
        parser.add_argument('--max_depth', type=int, default=3)
        run_parameters = vars(parser.parse_args())

        with mlflow.start_run():
            run_id = mlflow.active_run().info.run_id
            print(f"Run {run_id}:", f"Started with parameters {run_parameters}")
            print(f"Run {run_id}:", f"Training samples: {X_train.size}, Test samples: {X_test.size}")

            # create model instance: GBRT (Gradient Boosted Regression Tree) scikit-learn implementation
            model = GradientBoostingRegressor(**run_parameters)

            # Model Training
            model.fit(X_train, y_train)
            print(f"Run {run_id}:", "Training completed")

            # get evaluations scores
            score = rmse_score(y_test, model.predict(X_test))
            score_cv = rmse_cv_score(model, X_train, y_train)
            print(f"Run {run_id}:", "RMSE score: {:.4f}".format(score))
            print(f"Run {run_id}:",
                  "Cross-validation RMSE score: {:.4f} (std = {:.4f})".format(score_cv.mean(), score_cv.std()))

            # generate charts
            model_feature_importance(model)
            plt.close()
            model_permutation_importance(model)
            plt.close()
            model_tree_visualization(model)

            # log estimator name
            mlflow.set_tag("estimator_name", model.__class__.__name__)

            # log input features
            mlflow.set_tag("features", str(X_train.columns.values.tolist()))

            # Log tracked parameters only
            mlflow.log_params(run_parameters)

            mlflow.log_metrics({
                'RMSE_CV': score_cv.mean(),
                'RMSE': score,
            })

            # log training loss
            for s in model.train_score_:
                mlflow.log_metric("Train Loss", s)

            # get model signature
            signature = infer_signature(model_input=X_train, model_output=model.predict(X_train))

            # Save model to artifacts
            mlflow.sklearn.log_model(model, "model", signature=signature)

            # log charts
            # mlflow.log_artifacts(model_artifacts_dir)

            # optional: auto-logging for scikit-learn estimators
            # mlflow.sklearn.autolog()

            # optional: log all model parameters
            # mlflow.log_params(model.get_params())

            print(f"Run {run_id}:", "Logging completed")

else:
    print("Cannot run the selected model")