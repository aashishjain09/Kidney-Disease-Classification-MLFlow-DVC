
# Importing necessary libraries
import os, yaml, json, joblib, base64
from box.exceptions import BoxValueError
from cnnClassifier import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.
    
    Args:
        path_to_yaml (str): Path to the YAML file.
    
    Raises:
        ValueError: If the file does not exist or is not a valid YAML file.
        e: empty file
        
    Returns:
        ConfigBox: Contents of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty or not a valid YAML file.")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True) -> None:
    """
    Creates directories if they do not exist.
    
    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool): If True, prints the status of directory creation.
    """
    for directory in path_to_directories:
        os.makedirs(directory, exist_ok=True)
        if verbose:
            logger.info(f"Directory {directory} created successfully.")


@ensure_annotations
def save_json(path_to_json: Path, data: dict) -> None:
    """
    Saves a dictionary as a JSON file.
    
    Args:
        path_to_json (str): Path to the JSON file.
        data (dict): Dictionary to save as JSON.
    """
    with open(path_to_json, "w") as json_file:
        json.dump(data, json_file, indent=4)

    logger.info(f"JSON file {path_to_json} saved successfully.")


@ensure_annotations
def load_json(path_to_json: Path) -> ConfigBox:
    """
    Loads a JSON file and returns its contents as a dictionary.
    
    Args:
        path_to_json (str): Path to the JSON file.
    
    Returns:
        dict: Contents of the JSON file.
    """
    with open(path_to_json, "r") as json_file:
        data = json.load(json_file)

    logger.info(f"JSON file {path_to_json} loaded successfully.")
    return ConfigBox(data)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save a binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): Path to the saved binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved successfully at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load a binary file
    
    Args:
        path (Path): Path to the binary file
    
    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Determine the size of a file in kB
    
    Args:
        path (Path): Path to the file
    
    Returns:
        str: Size of the file in kBs
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} kB"


def decodeImage(imgString, fileName):
    imgData = base64.b64decode(imgString)
    with open(fileName, "wb") as f:
        f.write(imgData)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
