import streamlit as st
import plotly.express as px

def show_sales_comparison(df):
    st.subheader("📊 Perbandingan Penjualan per Merek")
    
    # Hitung unit
    sales_data = df['make'].value_counts().reset_index()
    sales_data.columns = ['Merek', 'Total Unit']
    
    # Plotting
    fig = px.bar(sales_data, x='Merek', y='Total Unit', 
                 color='Total Unit', 
                 color_continuous_scale='Viridis',
                 template="plotly_dark")
    
    st.plotly_chart(fig, use_container_width=True)