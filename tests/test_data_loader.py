# tests/test_data_loader.py
import pandas as pd
import pytest
from ml_data_pipeline.data_loader import DataLoaderFactory

@pytest.fixture
def sample_csv(tmp_path):
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text("feature1\tfeature2\ttarget\n1\t4\t0\n2\t5\t1\n3\t6\t0")
    return str(csv_file)

def test_csv_loader(sample_csv):
    loader = DataLoaderFactory.get_data_loader("csv")
    data = loader.load_data(sample_csv)  # Assuming default delimiter ','
    assert isinstance(data, pd.DataFrame)
    assert data.shape == (3, 3), "Data shape should be 3 rows by 3 columns"
