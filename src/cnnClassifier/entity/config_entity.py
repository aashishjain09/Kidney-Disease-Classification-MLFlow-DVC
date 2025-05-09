from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: Path
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    secondary_base_model_path: Path  # OUTSIDE ARTIFACTS
    updated_base_model_path: Path
    secondary_updated_base_model_path: Path  # OUTSIDE ARTIFACTS
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    param_weights: str
    params_classes: int


@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    secondary_trained_model_path: Path  # OUTSIDE ARTIFACTS
    updated_base_model_path: Path
    secondary_updated_base_model_path: Path  # OUTSIDE ARTIFACTS
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list


@dataclass(frozen=True)
class EvaluationConfig:
    path_of_model: Path
    training_data: Path
    all_params: dict
    mlflow_uri: str
    params_image_size: list
    params_batch_size: int