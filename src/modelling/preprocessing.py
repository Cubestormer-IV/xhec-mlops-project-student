import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from prefect import task

@task(name="preprocess-data", tags=["fails"], retries=3, retry_delay_seconds=60)
def preprocess_data(df):

    """
    Preprocesses the dataset by separating the features and the target variable, and applies transformations to prepare the data for modeling.

    This function separates the input dataframe into features (X) and the target variable (y), where the target is the 'Rings' column.
    It applies preprocessing steps including one-hot encoding for the categorical 'Sex' feature and scaling for numeric features such as
    'Length', 'Diameter', 'Height', and various weight-related columns. The function returns the processed features (X), target (y), and
    the preprocessing pipeline.

    Args:
        df (pd.DataFrame): The input dataframe containing the dataset.

    Returns:
        X (pd.DataFrame): The features of the dataset, with 'Sex' encoded and numeric features scaled.
        y (pd.Series): The target variable ('Rings').
        preprocessor (ColumnTransformer): The preprocessing pipeline that scales numerical features and encodes the 'Sex' feature.
    """

    # Separate features and target variable
    X = df.drop(columns='Rings')
    y = df['Rings']

    # Preprocess the 'Sex' feature using one-hot encoding and scale numeric features
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), ['Length', 'Diameter', 'Height', 'Whole weight',
                                        'Shucked weight', 'Viscera weight', 'Shell weight']),
            ('cat', OneHotEncoder(), ['Sex'])
        ]
    )

    return X, y, preprocessor
