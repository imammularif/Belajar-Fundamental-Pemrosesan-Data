import pandas as pd

def extract_data(file_path):
    print("Mengekstrak data dari CSV...")
    return pd.read_csv(file_path)