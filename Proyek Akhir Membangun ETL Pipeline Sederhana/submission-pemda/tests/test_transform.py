import pandas as pd
from utils.transform import transform_data

def test_transform_cleaning():
    # 1. Buat data contoh LENGKAP agar transform_data tidak error 'KeyError'
    data = {
        'name': ['T-shirt 1', 'Unknown Product', 'Hoodie 2', 'T-shirt 3'],
        'price': ['$10.00', '$5.00', 'Price Unavailable', '$20.00'],
        'rating': ['4.5 / 5', '4.0 / 5', '4.8 / 5', '3.5 / 5'],
        'colors': ['3 Colors', '2 Colors', '1 Color', '4 Colors'],
        'size': ['Size: M', 'Size: L', 'Size: S', 'Size: XL'],
        'gender': ['Gender: Men', 'Gender: Women', 'Gender: Unisex', 'Gender: Men']
    }
    df = pd.DataFrame(data)
    
    # 2. Jalankan transformasi
    df_cleaned = transform_data(df)
    
    # 3. VERIFIKASI:
    # Baris 'Unknown Product' dan 'Price Unavailable' (total 2 baris) harus terhapus.
    # Sisa baris harusnya tinggal 2.
    assert len(df_cleaned) == 2
    
    # Cek apakah harga berubah jadi Rupiah ($10 * 16000 = 160000)
    assert df_cleaned.iloc[0]['price'] == 160000.0
    
    # Cek apakah kolom rating jadi angka (float)
    assert isinstance(df_cleaned.iloc[0]['rating'], float)
    
    # Cek apakah kolom timestamp ada
    assert 'timestamp' in df_cleaned.columns