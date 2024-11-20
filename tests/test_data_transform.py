from ml_data_pipeline.data_transform import MinMaxScalerTransformer
import pandas as pd

def test_minmax_scaler():
    transformer = MinMaxScalerTransformer()
    data = pd.DataFrame({'value': [10, 20, 30]})
    transformed = transformer.transform(data)
    assert transformed['value'].min() == 0 and transformed['value'].max() == 1, "Data should be scaled between 0 and 1"
