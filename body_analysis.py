import streamlit as st
import plotly.express as px

def show_body_analysis(df):
    st.subheader("🚐 Analisis Berdasarkan Tipe Body Mobil")
    
    # 1. Daftar body yang diinginkan
    allowed_bodies = [
        'Coupe', 'Suv', 'Sedan', 'Hatchback', 'Wagon', 'Convertible', 
        'Crew Cab', 'Regular Cab', 'Extended Cab', 'Minivan', 
        'Quad Cab', 'Supercrew'
    ]
    
    # 2. Filter data (Case insensitive biar aman)
    df_body = df[df['body'].isin(allowed_bodies)].copy()
    
    # 3. Hitung jumlah unit per tipe body
    body_count = df_body['body'].value_counts().reset_index()
    body_count.columns = ['Tipe Body', 'Jumlah Unit']
    
    # 4. Visualisasi Pie Chart (biar variasi tidak batang terus)
    st.write("### Persentase Tipe Body di Pasar")
    fig_pie = px.pie(body_count, values='Jumlah Unit', names='Tipe Body', 
                     title="Distribusi Tipe Body",
                     hole=0.4, # Membuat Donut Chart agar lebih modern
                     template="plotly_dark")
    st.plotly_chart(fig_pie, use_container_width=True)
    
    # 5. Visualisasi Bar Chart (Urutan terbanyak)
    st.write("### Ranking Jumlah per Tipe Body")
    fig_bar = px.bar(body_count, x='Tipe Body', y='Jumlah Unit', 
                     color='Jumlah Unit',
                     color_continuous_scale='Blues',
                     template="plotly_white")
    st.plotly_chart(fig_bar, use_container_width=True)