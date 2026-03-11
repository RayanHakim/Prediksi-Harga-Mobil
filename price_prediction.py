import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import joblib

def show_price_prediction(df):
    st.subheader("🤖 AI Price Predictor (Machine Learning)")
    st.write("Model ini memprediksi harga jual berdasarkan brand, tahun, kondisi, dan odometer.")

    # 1. Persiapan Data (Hanya ambil fitur penting)
    ml_df = df[['year', 'make', 'condition', 'odometer', 'sellingprice']].dropna()
    
    # Label Encoding untuk data teks (Make) agar jadi angka
    le = LabelEncoder()
    ml_df['make_encoded'] = le.fit_transform(ml_df['make'])
    
    # 2. Sidebar Input untuk User
    st.sidebar.markdown("---")
    st.sidebar.subheader("Input Spesifikasi")
    input_make = st.sidebar.selectbox("Pilih Merek", df['make'].unique())
    input_year = st.sidebar.slider("Tahun Kendaraan", 1990, 2015, 2010)
    input_cond = st.sidebar.slider("Kondisi (1-5)", 1.0, 5.0, 3.5)
    input_km = st.sidebar.number_input("Odometer (Mil)", value=50000)

    # 3. Tombol Training & Prediksi
    if st.button("🚀 Hitung Estimasi Harga"):
        with st.spinner('AI sedang menghitung...'):
            # Fitur (X) dan Target (y)
            X = ml_df[['year', 'make_encoded', 'condition', 'odometer']]
            y = ml_df['sellingprice']
            
            # Kita gunakan sampel agar training cepat (karena data 558rb baris)
            model = RandomForestRegressor(n_estimators=50, random_state=42)
            model.fit(X.head(50000), y.head(50000)) # Ambil 50rb sampel agar ringan
            
            # Siapkan data input user
            user_input = [[input_year, le.transform([input_make])[0], input_cond, input_km]]
            prediction = model.predict(user_input)
            
            st.success(f"### Estimasi Harga Jual: ${prediction[0]:,.2f}")
            st.balloons()

            # Tampilkan tingkat pengaruh (Feature Importance)
            st.write("**Faktor yang paling berpengaruh terhadap harga:**")
            importance = pd.DataFrame({'Fitur': X.columns, 'Importance': model.feature_importances_})
            st.bar_chart(importance.set_index('Fitur'))