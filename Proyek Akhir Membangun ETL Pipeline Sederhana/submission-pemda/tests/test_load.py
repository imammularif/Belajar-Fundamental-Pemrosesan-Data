import pytest
from utils.load import load_to_sheets

def test_load_function_exists():
    # Hanya mengetes apakah fungsi load bisa diimport dan ada
    assert callable(load_to_sheets)