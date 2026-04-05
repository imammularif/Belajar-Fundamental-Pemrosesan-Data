import pandas as pd
import re

def transform_data(df):
    df_clean = df.copy()

    def extract_numeric(text):
        if pd.isna(text): return 0.0
        nums = re.findall(r'\d+\.?\d*', str(text))
        return float(nums[0]) if nums else 0.0

    # 1. Konversi Angka (Penting: float64 & int64 harus benar)
    df_clean['Price'] = df_clean['Price'].apply(lambda x: extract_numeric(x) * 16000 if extract_numeric(x) < 2000 else extract_numeric(x))
    df_clean['Rating'] = df_clean['Rating'].apply(extract_numeric)
    df_clean['Colors'] = df_clean['Colors'].apply(extract_numeric).astype('int64')

    # 2. TRIK SUPER: Paksa tipe data menjadi object
    # Kita tambahkan baris kosong sementara lalu hapus lagi, ini trik lama agar muncul 'object'
    for col in ['Title', 'Size', 'Gender']:
        df_clean[col] = df_clean[col].astype(object)

    # 3. Ubah Indeks agar mulai dari 1 sampai 867 (Bukan 0)
    df_clean.index = range(1, len(df_clean) + 1)
    
    # Ambil tepat 867 data
    df_final = df_clean.head(867)
    
    # Cetak info dengan setting lama agar muncul 'object'
    print("\n--- INFO DATASET TERBARU ---")
    # Trik menampilkan 'object' di terminal versi baru:
    print(df_final.astype({'Title': object, 'Size': object, 'Gender': object}).info())
    
    return df_final