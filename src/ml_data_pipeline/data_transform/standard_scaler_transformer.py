from sklearn.preprocessing import StandardScaler
from .base_transformer import DataTransformer
import pandas as pd


class StandardScalerTransformer(DataTransformer):
    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(data)
        return pd.DataFrame(scaled_data, columns=data.columns)
