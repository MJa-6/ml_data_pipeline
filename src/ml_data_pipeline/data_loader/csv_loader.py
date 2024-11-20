# src/ml_data_pipeline/data_loader/csv_loader.py
import pandas as pd
from loguru import logger
from .base_loader import DataLoader

class CSVLoader(DataLoader):
    def load_data(self, file_path: str, delimiter='\t') -> pd.DataFrame:
        """Load data from a CSV file.

        Args:
            file_path (str): Path to the CSV file.
            delimiter (str, optional): Delimiter to use. Defaults to ','.

        Returns:
            pd.DataFrame: Loaded data as DataFrame.
        """
        logger.info(f"Loading data from CSV file at {file_path}")
        try:
            data = pd.read_csv(file_path, delimiter=delimiter)
            logger.info(f"Successfully loaded data from {file_path}")
            return data
        except Exception as e:
            logger.error(f"Error loading data from {file_path}: {e}")
            raise
