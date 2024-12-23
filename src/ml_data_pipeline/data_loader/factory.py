from .csv_loader import CSVLoader
from .json_loader import JSONLoader
from .base_loader import DataLoader


class DataLoaderFactory:
    @staticmethod
    def get_data_loader(file_type: str) -> DataLoader:
        if file_type == "csv":
            return CSVLoader()
        elif file_type == "json":
            return JSONLoader()
        else:
            raise ValueError("Unsupported file type")
