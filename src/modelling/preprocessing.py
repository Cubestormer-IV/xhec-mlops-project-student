import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def preprocess_data(df):
    """Preprocess the dataset and return the features and target variable."""

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
