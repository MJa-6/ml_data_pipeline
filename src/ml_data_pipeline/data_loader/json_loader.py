import json
import pandas as pd
from loguru import logger
from .base_loader import DataLoader


class JSONLoader(DataLoader):
    def load_data(self, file_path: str) -> pd.DataFrame:
        logger.info(f"Attempting to load JSON data from {file_path}")
        try:
            with open(file_path, "r") as file:
                data_dict = json.load(file)
            data = pd.DataFrame(data_dict)
            logger.info(f"Data successfully loaded from {file_path}")
            return data
        except Exception as e:
            logger.error(f"Failed to load JSON data from {file_path}: {e}")
            raise
