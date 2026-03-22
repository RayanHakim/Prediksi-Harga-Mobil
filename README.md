# 🚗 Car Market Analytics & AI Price Prediction Dashboard

Dashboard analitik komprehensif yang dibangun menggunakan **Streamlit** untuk memproses, memvisualisasikan, dan memprediksi tren pasar mobil berdasarkan dataset harga historis. Proyek ini mendemonstrasikan alur kerja *Data Science* end-to-end, mulai dari pembersihan data hingga implementasi model *Machine Learning*.

---

## 🌟 Fitur Utama

Aplikasi ini dibagi menjadi beberapa modul analisis interaktif:

* **🏠 Home & Data Catalog:** Ringkasan dataset dan tampilan sampel unit unik untuk setiap merek mobil yang tersedia dalam database.
* **📊 Sales Comparison:** Visualisasi perbandingan volume penjualan antar merek mobil untuk melihat penguasa pasar.
* **💰 Price Analysis:** Analisis mendalam mengenai distribusi harga dan korelasi antar variabel.
* **🚐 Body Type Analysis:** Klasifikasi dan tren pasar berdasarkan tipe bodi kendaraan (SUV, Sedan, Hatchback, dll.).
* **🤖 AI Price Prediction:** Implementasi model *Machine Learning* untuk memprediksi harga jual mobil berdasarkan input spesifikasi pengguna.

---

## 🛠️ Arsitektur Proyek (Modular Design)

Proyek ini dirancang dengan prinsip **Clean Architecture** agar kode mudah dikelola dan dikembangkan:

| Nama File | Fungsi / Tanggung Jawab |
| :--- | :--- |
| `app.py` | *Main Entry Point* dan konfigurasi navigasi Sidebar. |
| `data_loader.py` | Menangani proses *loading* dan *preprocessing* dataset CSV. |
| `sales_chart.py` | Logika visualisasi grafik perbandingan penjualan. |
| `price_analysis.py` | Modul analisis statistik harga kendaraan. |
| `body_analysis.py` | Analisis segmentasi pasar berdasarkan tipe bodi. |
| `price_prediction.py` | Implementasi model prediksi harga berbasis AI. |

---

## 🧪 Tech Stack
* **Framework:** [Streamlit](https://streamlit.io/)
* **Data Manipulation:** [Pandas](https://pandas.pydata.org/), NumPy
* **Visualization:** Plotly / Matplotlib / Seaborn
* **Machine Learning:** Scikit-Learn
* **Language:** Python 3.x

---

## 🚀 Cara Menjalankan

1.  **Clone Repositori:**
    ```bash
    git clone [https://github.com/RayanHakim/Car-Market-Dashboard.git](https://github.com/RayanHakim/Car-Market-Dashboard.git)
    cd Car-Market-Dashboard
    ```

2.  **Instalasi Library:**
    ```bash
    pip install streamlit pandas numpy scikit-learn plotly matplotlib seaborn
    ```

3.  **Jalankan Dashboard:**
    ```bash
    streamlit run app.py
    ```

---

## 👨‍💻 Developer
**Rayan Hakim**
*Data Scientist & Software Developer*
