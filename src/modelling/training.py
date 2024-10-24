import os
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
from preprocessing import preprocess_data
from prefect import task

@task(name="train-model", tags=["fails"], retries=3, retry_delay_seconds=60)
def train_model(X,y, preprocessor, alpha, test_size, random_state):

    """
    Trains a Lasso regression model using a given preprocessor and splits the data into training and test sets.

    This function accepts the input features (X), target variable (y), and a preprocessor pipeline.
    It splits the data into training and test sets, creates a machine learning pipeline that first applies
    the preprocessor to the data, and then fits a Lasso regression model. After training, the function returns
    the trained pipeline along with the split data.

    Args:
        X (pd.DataFrame): The input features.
        y (pd.Series): The target variable (e.g., regression labels).
        preprocessor (Pipeline): The preprocessing pipeline that will be applied to the data before training.

    Returns:
        pipeline (Pipeline): The trained pipeline containing the preprocessor and the Lasso regression model.
        X_train (pd.DataFrame): The training data (features).
        X_test (pd.DataFrame): The test data (features).
        y_train (pd.Series): The training data (target variable).
        y_test (pd.Series): The test data (target variable).
    """


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    model = Lasso(alpha=alpha)

    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', model)
    ])

    pipeline.fit(X_train, y_train)
    return pipeline, X_train, X_test, y_train, y_test


#if __name__ == "__main__":
  #  import sys
    #train_model(sys.argv[1])  # Pass the training dataset path as argument
