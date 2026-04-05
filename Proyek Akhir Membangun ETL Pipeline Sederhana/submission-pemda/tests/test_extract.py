import pytest
import pandas as pd
from utils.extract import extract_data
import os

def test_extract_data_success():
    # Pastikan file CSV ada sebelum dites
    file_path = "products.csv"
    if os.path.exists(file_path):
        df = extract_data(file_path)
        assert isinstance(df, pd.DataFrame)
        assert not df.empty
    else:
        pytest.skip("File products.csv tidak ditemukan, skip test ini.")