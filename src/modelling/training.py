import os
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
from preprocessing import preprocess_data

def train_model(X,y, preprocessor):
        
        alpha = 0.01
        test_size = 0.2
        random_state = 50
    
        
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