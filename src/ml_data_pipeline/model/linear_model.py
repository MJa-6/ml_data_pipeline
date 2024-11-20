# src/ml_data_pipeline/model/linear_model.py
import pandas as pd
from .base_model import Model


class LinearModel(Model):
    """A Linear model with dummy parameters.

    Args:
        data (pd.DataFrame): A pandas DataFrame containing the data for prediction.

    Returns:
        pd.DataFrame: A DataFrame with model predictions.
    """

    def predict(self, data: pd.DataFrame) -> pd.DataFrame:
        print("Predicting with Linear Model")
        # Dummy implementation for prediction
        return data.assign(Prediction=data["Feature1"] * 0.5)
