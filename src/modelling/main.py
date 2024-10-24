# This module is the training flow: it reads the data, preprocesses it, trains a model and saves it.

import argparse
from training import *
from utils import *
from preprocessing import *


def main(trainset_path) -> None:
    """Train a model using the data at the given path and save the model (pickle)."""
    # Read data
    file_path = '../data/abalone.csv'
    df = pd.read_csv(trainset_path)

    # Preprocess data
    X,y, preprocessor = preprocess_data(df)
    
    # (Optional) Pickle encoder if need be

    # Train model
    pipeline, X_train, X_test, y_train, y_test = train_model(X,y, preprocessor)

    # Pickle model --> The model should be saved in pkl format the `src/web_service/local_objects` folder
    pickle_object(pipeline)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a model using the data at the given path.")
    parser.add_argument("trainset_path", type=str, help="Path to the training set")
    args = parser.parse_args()
    main(args.trainset_path)



