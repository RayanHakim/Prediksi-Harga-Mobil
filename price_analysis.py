import streamlit as st
import plotly.express as px

def show_price_analysis(df):
    st.subheader("💰 Analisis Rata-rata Harga Jual")
    
    # Hitung rata-rata harga per brand
    avg_price = df.groupby('make')['sellingprice'].mean().sort_values(ascending=False).reset_index()
    
    fig = px.bar(avg_price, x='make', y='sellingprice', 
                 title="Rata-rata Harga per Merek (USD)",
                 labels={'make': 'Merek', 'sellingprice': 'Harga Rata-rata'},
                 template="plotly_white")
    
    st.plotly_chart(fig, use_container_width=True)