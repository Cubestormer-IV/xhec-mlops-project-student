import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

import sys
sys.path.insert(1, 'C:/Users/USER/Documents/HEC/MLOPS/xhec-mlops-project-student')

from src.web_service.lib.models import InputSchema, PredictionResponseSchema
from src.web_service.utils import load_object
from pathlib import Path


MODEL_PATH = "local_objects/model.pkl"

def get_input_df(payload: InputSchema) -> pd.DataFrame:
    """Convert 'InputSchema' object to the pandas dataframe.

    Parameters
    ----------
    payload : InputSchema
        The model input.

    Returns
    -------
    input_df : pd.DataFrame
        The model input converted to the pandas DataFrame.
    """
    input_df = pd.DataFrame(
        [
            {   
                "Sex": payload.Sex,
                "Length": payload.Length,
                "Diameter": payload.Diameter,
                "Height": payload.Height,
                "Whole weight": payload.Whole_weight,
                "Shucked weight": payload.Shucked_weight,
                "Viscera weight": payload.Viscera_weight,
                "Shell weight": payload.Shell_weight
                
            }
        ]
    )

    return input_df



def preprocessing() -> pd.DataFrame:
    """Preprocess the dataset and return the features and target variable."""
    
    # Separate features and target variable
    
    # Preprocess the 'Sex' feature using one-hot encoding and scale numeric features
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), ['Length', 'Diameter', 'Height', 'Whole weight',
                                       'Shucked weight', 'Viscera weight', 'Shell weight']),
            ('cat', OneHotEncoder(), ['Sex'])
        ]
    )

    return preprocessor



def infer_age(payload: InputSchema) -> PredictionResponseSchema:
    """Predict abalone age.

    Parameters
    ----------
    payload : InputSchema
        Model input object. Encapsulates input features.

    Returns
    -------
    prediction : PredictionResponseSchema
        Model output object. Encapsulates predicted age.
    """
    

    model = load_object(MODEL_PATH)

    df = get_input_df(payload)
    y_pred = model.predict(df)
    
    prediction = PredictionResponseSchema(predicted_age=y_pred[0])

    return prediction