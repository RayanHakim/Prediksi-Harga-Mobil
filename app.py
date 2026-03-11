import streamlit as st
# Import fungsi dari file lain di folder yang sama
from data_loader import get_clean_data
from sales_chart import show_sales_comparison
from price_analysis import show_price_analysis
from body_analysis import show_body_analysis
from price_prediction import show_price_prediction 

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Sistem Analisis Merek Mobil", 
    page_icon="🚗", 
    layout="wide"
)

# 2. Judul Utama
st.title("🚗 Dashboard Analisis Pasar Mobil")
st.markdown("---")

# 3. Load Data
try:
    # Menggunakan nama file CSV hasil pembersihan kamu
    df = get_clean_data('car_prices_fix.csv')

    # 4. Sidebar Navigasi
    st.sidebar.title("🧭 Navigasi")
    menu = st.sidebar.radio(
        "Pilih Analisis:", 
        [
            "Home", 
            "Perbandingan Penjualan", 
            "Analisis Harga", 
            "Analisis Tipe Body",
            "Prediksi Harga (AI)"
        ]
    )

    # 5. Logika Menu
    if menu == "Home":
        st.write("### 🏠 Selamat Datang!")
        st.write(f"Dataset berhasil dimuat dengan total **{len(df):,}** baris data bersih.")
        
        st.markdown("---")
        st.subheader("📌 Katalog Sampel per Merek")
        st.write("Berikut adalah tampilan satu contoh unit (data unik) untuk setiap merek mobil yang tersedia:")

        # Mengambil masing-masing satu baris untuk setiap merek agar rapi
        df_unique = df.drop_duplicates(subset=['make']).sort_values('make')

        # Menampilkan tabel yang rapi dan interaktif
        st.dataframe(df_unique, use_container_width=True)
        
        st.info(f"Ditemukan total **{len(df_unique)}** merek mobil dalam database ini.")

    elif menu == "Perbandingan Penjualan":
        show_sales_comparison(df)

    elif menu == "Analisis Harga":
        show_price_analysis(df)
        
    elif menu == "Analisis Tipe Body":
        show_body_analysis(df)

    elif menu == "Prediksi Harga (AI)":
        # Memanggil fitur Machine Learning
        show_price_prediction(df)

except Exception as e:
    st.error(f"⚠️ Terjadi Kesalahan: {e}")
    st.info("Pastikan semua file .py (data_loader, sales_chart, price_analysis, body_analysis, price_prediction) berada di folder yang sama.")

# 6. Footer Sidebar
st.sidebar.markdown("---")
st.sidebar.write("Sistem Prediksi Harga Mobil")