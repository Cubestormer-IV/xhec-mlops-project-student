# This module is the training flow: it reads the data, preprocesses it, trains a model and saves it.

import argparse
from training import *
from utils import *
from preprocessing import *
from predicting import *

import mlflow
from prefect import flow
from mlflow import MlflowClient

@flow(name="training-pipeline", retries=3, retry_delay_seconds=5, log_prints=True)
def main(trainset_path) -> None:

    """
    Train a Lasso regression model using the dataset provided at the specified path, log relevant parameters and metrics using MLflow,
    and save the trained model and preprocessor as pickle files.

    This function performs the following steps:
    1. Sets up an MLflow experiment for tracking model training and logging.
    2. Reads the training dataset from the specified path.
    3. Preprocesses the data for training.
    4. Trains a Lasso regression model.
    5. Logs model parameters, metrics, and the trained model to MLflow.
    6. Saves the preprocessor and trained model as pickle files for later use.

    Args:
        trainset_path (str): The path to the training dataset in CSV format.

    Returns:
        None: The function does not return any value.

    Example usage:
        python script.py ../data/abalone.csv
    """


    # Set the experiment
    mlflow.set_experiment("abalone-model")

    # Start an MLflow run
    with mlflow.start_run() as run:
        run_id = run.info.run_id

        mlflow.set_tags({
            "model": "Lasso Regression",
            "version": "1.0",
            "author": " ",
            "description": "Lasso regression model training and logging example"
        })


        """Train a model using the data at the given path and save the model (pickle)."""
        # Read data
        file_path = '../data/abalone.csv'
        df = pd.read_csv(trainset_path)

        # Preprocess data
        X,y, preprocessor = preprocess_data(df)

        # Log parameters manually
        mlflow.log_param("alpha", alpha)
        mlflow.log_param("test_size", test_size)
        mlflow.log_param("random_state", random_state)

        # Train model
        model, X_train, X_test, y_train, y_test = train_model(X,y, preprocessor)

        # Predict on the test set

        y_pred = predict(model, X_train, X_test, y_train, y_test)

        # Evaluate the model using Mean Squared Error
        rmse = root_mean_squared_error(y_test, y_pred)

        # Log metrics manually
        mlflow.log_metric("rmse", rmse)

        # Log the model
        mlflow.sklearn.log_model(pipeline, "models")

        # Register the model
        mlflow.register_model(f"runs:/{run_id}/models", "lasso_model")

    # Pickle encoder
    pickle_object(preprocessor, "preprocessor")

    # Pickle model --> The model should be saved in pkl format the `src/web_service/local_objects` folder
    pickle_object(model, "model")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a model using the data at the given path.")
    parser.add_argument("trainset_path", type=str, help="Path to the training set")
    args = parser.parse_args()
    main(args.trainset_path)
