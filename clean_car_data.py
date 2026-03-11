import pandas as pd
import os

def clean_to_csv_pro(input_file, output_file):
    print(f"🚀 Memproses file besar: {input_file}...")
    
    # 1. Load Data
    df = pd.read_csv(input_file, on_bad_lines='skip', low_memory=False)

    # 2. Merapikan Tanggal (saledate)
    if 'saledate' in df.columns:
        print("📅 Merapikan format tanggal...")
        df['saledate'] = df['saledate'].str.slice(0, 15)
        df['saledate'] = pd.to_datetime(df['saledate'], errors='coerce').dt.date

    # 3. Standarisasi Teks
    print("🔠 Standarisasi teks (Capitalize)...")
    for col in ['make', 'model', 'trim', 'body', 'color']:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.title()

    # 4. Filter Kolom
    cols_to_keep = [
        'year', 'make', 'model', 'trim', 'body', 'transmission', 
        'state', 'condition', 'odometer', 'color', 'interior', 
        'mmr', 'sellingprice', 'saledate'
    ]
    existing_cols = [c for c in cols_to_keep if c in df.columns]
    df_final = df[existing_cols].copy() # Pakai copy biar aman saat sorting

    # 5. FITUR BARU: Urutkan Abjad (Make then Model)
    print("📑 Mengurutkan data berdasarkan Merk dan Model...")
    df_final = df_final.sort_values(by=['make', 'model'], ascending=True)

    # 6. Simpan ke CSV (Format Titik Koma untuk Excel Indonesia)
    print(f"📁 Menyimpan file rapi ke: {output_file}")
    df_final.to_csv(output_file, index=False, sep=';', encoding='utf-8-sig')
    
    print("✅ SELESAI! Data sudah urut abjad dan siap dianalisis.")

if __name__ == "__main__":
    input_name = 'car_prices.csv'
    output_name = 'car_prices_fix.csv'
    
    if os.path.exists(input_name):
        clean_to_csv_pro(input_name, output_name)
    else:
        print(f"❌ File {input_name} tidak ditemukan di folder ini.")