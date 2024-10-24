import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.pipeline import Pipeline
from src.modelling.preprocessing import preprocess_data
from utils import load_model


def predict(pipeline, X_train, X_test, y_train, y_test) -> None:
    # Load the model
    model = pipeline
    prediction = model.predict(X_test)
    return prediction

     
    

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Predict using the trained model.")
    parser.add_argument("data_path", type=str, help="Path to the data for prediction")
    parser.add_argument("model_uri", type=str, help="URI of the trained model in MLflow")
    args = parser.parse_args()
    predict(args.data_path, args.model_uri)