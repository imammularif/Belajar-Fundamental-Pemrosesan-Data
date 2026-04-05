import gspread
from google.oauth2.service_account import Credentials

def load_to_sheets(df, sheet_url, json_file):
    print("Mengirim data ke Google Sheets...")
    scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive"]
    
    try:
        # Load kredensial dari file JSON
        creds = Credentials.from_service_account_file(json_file, scopes=scope)
        client = gspread.authorize(creds)
        
        # Buka spreadsheet menggunakan variabel sheet_url (pastikan pakai tanda kutip di main.py)
        # Gunakan link murni sampai bagian /edit saja agar gspread tidak bingung
        clean_url = sheet_url.split("?")[0].split("#")[0]
        sheet = client.open_by_url(clean_url).get_worksheet(0) 
        
        # Bersihkan data lama agar data baru 867 baris masuk dengan rapi
        sheet.clear()
        
        # Format data: Header + Data
        header = df.columns.values.tolist()
        values = df.values.tolist()
        data_to_upload = [header] + values
        
        # Kirim ke Sheets
        sheet.update('A1', data_to_upload)
        print("✅ Berhasil Sinkronisasi ke Google Sheets!")
        
    except Exception as e:
        print(f"❌ Gagal update Google Sheets: {e}")

def load_to_csv(df, filename):
    df.to_csv(filename, index=False)
    print(f"✅ Berhasil menyimpan {len(df)} data ke {filename}")