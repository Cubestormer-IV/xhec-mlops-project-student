import os
import pickle
from functools import lru_cache
from loguru import logger
from prefect import task

@task(name="save-pickle", tags=["fails"], retries=3, retry_delay_seconds=60)
def pickle_object(obj: object, filename: str, folder_path: str = '../web_service/local_objects') -> None:
    """
    Pickles and saves the given object to a specified folder.

    Args:
        obj (object): The object to pickle.
        filename (str): The name of the file to save the object to, without extension.
        folder_path (str): The directory path where the file will be saved. Defaults to '../web_service/local_objects'.
    """
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, f"{filename}.pkl")
    try:
        with open(file_path, 'wb') as f:
            pickle.dump(obj, f)
        logger.info(f"Object saved to {file_path}")
    except Exception as e:
        logger.error(f"Failed to pickle object: {e}")

@task(name="load-preprocessor", tags=["fails"], retries=3, retry_delay_seconds=60)
@lru_cache
def load_preprocessor(filepath: os.PathLike) -> object:
    """
    Loads a pickled preprocessor from the specified file path.

    Args:
        filepath (os.PathLike): The path to the pickled preprocessor file.

    Returns:
        object: The loaded preprocessor.
    """
    logger.info(f"Loading preprocessor from {filepath}")
    try:
        with open(filepath, "rb") as f:
            return pickle.load(f)
    except Exception as e:
        logger.error(f"Failed to load preprocessor: {e}")
        raise

@task(name="load-pickle-model", tags=["fails"], retries=3, retry_delay_seconds=60)
@lru_cache
def load_model(filepath: os.PathLike) -> object:
    """
    Loads a pickled model from the specified file path.

    Args:
        filepath (os.PathLike): The path to the pickled model file.

    Returns:
        object: The loaded model.
    """
    logger.info(f"Loading model from {filepath}")
    try:
        with open(filepath, "rb") as f:
            return pickle.load(f)
    except Exception as e:
        logger.error(f"Failed to load model: {e}")
        raise
