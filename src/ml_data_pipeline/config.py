from typing import Dict, Any, cast
from pydantic import BaseModel, validator
from omegaconf import OmegaConf
import os


class DataLoaderConfig(BaseModel):
    file_path: str
    file_type: str

    @validator("file_type")
    def validate_file_type(cls, value):
        assert value in {"csv", "json"}, "file_type must be 'csv' or 'json'"
        return value


class TransformationConfig(BaseModel):
    normalize: bool
    scaling_method: str

    @validator("scaling_method")
    def validate_scaling_method(cls, value):
        assert value in {
            "standard",
            "minmax",
        }, "scaling_method must be 'standard' or 'minmax'"
        return value


class Config(BaseModel):
    data_loader: DataLoaderConfig
    transformation: TransformationConfig


def load_config(config_path: str) -> Config:
    # Assumes config directory is at the project root.
    base_dir = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
    full_path = os.path.join(base_dir, config_path)
    raw_config = OmegaConf.load(full_path)
    config_dict = OmegaConf.to_container(raw_config, resolve=True)
    # Ensure the returned container is a dictionary
    if not isinstance(config_dict, dict):
        raise ValueError("Configuration must be a dictionary")

    # Use casting to help mypy understand the expected type
    typed_config_dict = cast(Dict[str, Any], config_dict)
    return Config(**typed_config_dict)
