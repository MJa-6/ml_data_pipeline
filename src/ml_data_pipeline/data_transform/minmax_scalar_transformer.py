from sklearn.preprocessing import MinMaxScaler
from .base_transformer import DataTransformer
import pandas as pd


class MinMaxScalerTransformer(DataTransformer):
    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        scaler = MinMaxScaler()
        scaled_data = scaler.fit_transform(data)
        return pd.DataFrame(scaled_data, columns=data.columns)
