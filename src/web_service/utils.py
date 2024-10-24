import os
import pickle
from functools import lru_cache
from loguru import logger


@lru_cache
def load_object(filepath: os.PathLike) -> object:
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