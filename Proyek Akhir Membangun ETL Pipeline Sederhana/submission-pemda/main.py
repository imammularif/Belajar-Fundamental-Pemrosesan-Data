from utils.scraper import scrape_data
from utils.transform import transform_data
from utils.load import load_to_sheets, load_to_csv
import pandas as pd

# Konfigurasi File & URL
CSV_FILE = "products.csv"
GOOGLE_JSON = "google-sheets-api.json"
# Link asli kamu (Kode di load.py akan otomatis membersihkan parameter ?gid=0)
SHEET_URL = "\#"
WEB_URL = "https://fashion-studio.dicoding.dev/"

def run_pipeline():
    # 1. EXTRACT
    print("--- TAHAP EXTRACT ---")
    raw_data = scrape_data(WEB_URL) 
    
    # Validasi jika data tidak ditemukan
    if not raw_data or len(raw_data) == 0:
        print("❌ Gagal: Data kosong. Cek pola URL (page-1.html) atau tag HTML di scraper.py.")
        return
        
    df_raw = pd.DataFrame(raw_data)
    print(f"Berhasil mengekstrak {len(df_raw)} data mentah.")
    
    # 2. TRANSFORM
    print("\n--- TAHAP TRANSFORM ---")
    # Mengubah teks jadi angka, konversi rupiah, dan filter 6 kolom kapital
    df_ready = transform_data(df_raw)
    
    if df_ready.empty:
        print("❌ Gagal: Data hilang setelah proses Transform.")
        return

    # 3. LOAD
    print("\n--- TAHAP LOAD ---")
    # Simpan ke CSV lokal
    load_to_csv(df_ready, CSV_FILE)
    
    # Kirim ke Google Sheets
    # Pastikan email di google-sheets-api.json sudah di-SHARE ke spreadsheet sebagai Editor
    load_to_sheets(df_ready, SHEET_URL, GOOGLE_JSON)

    print("\n✅ ETL SELESAI!")
    print(f"Total baris yang diproses: {len(df_ready)}")
    print("Silakan cek products.csv dan Google Sheets kamu.")

if __name__ == "__main__":
    run_pipeline()