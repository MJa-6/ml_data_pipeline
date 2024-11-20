from .standard_scaler_transformer import StandardScalerTransformer
from .minmax_scalar_transformer import MinMaxScalerTransformer
from .base_transformer import DataTransformer


class TransformerFactory:
    @staticmethod
    def get_transformer(scaling_method: str) -> DataTransformer:
        if scaling_method == "standard":
            return StandardScalerTransformer()
        elif scaling_method == "minmax":
            return MinMaxScalerTransformer()
        else:
            raise ValueError("Unsupported scaling method")
