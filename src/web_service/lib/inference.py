import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.web_service.lib.models import ModelInput, ModelOutput
from src.web_service.utils import load_object
from pathlib import Path


MODEL_PATH = "../local_objects/model.pkl" #to be adapted

def get_input_df(payload: ModelInput) -> pd.DataFrame:
    """Convert 'ModelInput' object to the pandas dataframe.

    Parameters
    ----------
    payload : ModelInput
        The model input.

    Returns
    -------
    input_df : pd.DataFrame
        The model input converted to the pandas DataFrame.
    """
    input_df = pd.DataFrame(
        [
            {   
                "Sex": payload.sex,
                "Length": payload.length,
                "Diameter": payload.diameter,
                "Height": payload.height,
                "Whole weight": payload.whole_weight,
                "Shucked weight": payload.shucked_weight,
                "Viscera weight": payload.viscera_weight,
                "Shell weight": payload.shell_weight
                
            }
        ]
    )

    return input_df



def preprocessing(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocess the dataset and return the features and target variable."""

    # Preprocess the 'Sex' feature using one-hot encoding and scale numeric features
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), ['Length', 'Diameter', 'Height', 'Whole weight',
                                        'Shucked weight', 'Viscera weight', 'Shell weight']),
            ('cat', OneHotEncoder(), ['Sex'])
        ]
    )

    return preprocessor


def infer_age(payload: ModelInput) -> ModelOutput:
    """Predict abalone age.

    Parameters
    ----------
    payload : ModelInput
        Model input object. Encapsulates input features.

    Returns
    -------
    prediction : ModelOutput
        Model output object. Encapsulates predicted age.
    """

    model = load_object(MODEL_PATH)

    df = get_input_df(payload)
    x= preprocessing(df)

    y_pred = model.predict(x)[0]
    prediction = ModelOutput(abalone_age=y_pred)

    return prediction