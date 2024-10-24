# Use this module to code a `pickle_object` function. This will be useful to pickle the model (and encoder if need be).
import os
import pickle
from functools import lru_cache
from loguru import logger


def pickle_object(obj, filename, folder_path='../web_service/local_objects'):
    # Ensure the folder exists
    os.makedirs(folder_path, exist_ok=True)

    # Full path to save the file
    file_path = os.path.join(folder_path, f"{filename}.pkl")

    # Save the object to the file
    with open(file_path, 'wb') as f:
        pickle.dump(obj, f)

    print(f"Object saved to {file_path}")


@lru_cache
def load_preprocessor(filepath: os.PathLike):
    logger.info(f"Loading preprocessor from {filepath}")
    with open(filepath, "rb") as f:
        return pickle.load(f)


@lru_cache
def load_model(filepath: os.PathLike):
    logger.info(f"Loading model from {filepath}")
    with open(filepath, "rb") as f:
        return pickle.load(f)