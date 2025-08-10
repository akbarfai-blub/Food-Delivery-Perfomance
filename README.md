# Dashboard Analitis untuk Optimalisasi Waktu Pengiriman Makanan

![Dashboard Screenshot]

Sebuah dashboard interaktif yang dibangun menggunakan Streamlit untuk menganalisis faktor-faktor kunci yang memengaruhi waktu pengiriman makanan, berdasarkan dataset dari Kaggle.

---

### 🔗 Live Demo

**[Lihat Dashboard Langsung di Sini!](URL)**

---

### 📝 Latar Belakang Proyek

Dalam industri logistik makanan yang kompetitif, efisiensi waktu pengiriman adalah kunci untuk kepuasan pelanggan dan profitabilitas. Proyek ini bertujuan untuk membedah data operasional pengiriman untuk menjawab pertanyaan fundamental: **Faktor apa saja yang paling signifikan memperlambat atau mempercepat pengiriman, dan bagaimana kita bisa memitigasi risikonya?**

Proyek ini merupakan output untuk jalur **Data Analyst**, di mana fokus utamanya adalah pada Eksplorasi Data (EDA), penemuan _insight_, dan penyajian temuan dalam bentuk dashboard interaktif yang mudah digunakan oleh tim operasional.

---

### ✨ Fitur Utama Dashboard

Dashboard ini dirancang untuk memberikan _insight_ secara cepat dan memungkinkan eksplorasi data secara mandiri. Fitur utamanya meliputi:

- **📈 Metrik Utama (KPIs):** Tampilan ringkas untuk Total Pengiriman, Rata-rata Waktu Kirim, dan Rata-rata Jarak.
- **📊 Filter Interaktif:** Pengguna dapat memfilter data secara dinamis berdasarkan **Kondisi Cuaca** dan **Tingkat Lalu Lintas**.
- **🌐 Visualisasi Plotly:** Semua grafik bersifat interaktif, memungkinkan pengguna untuk melakukan _hover_ untuk melihat detail, serta _zoom_ dan _pan_.
- **🔍 Analisis Mendalam:** Menyajikan visualisasi untuk hubungan antar variabel, dari korelasi sederhana hingga efek interaksi yang kompleks.
- **📋 Tampilan Data Mentah:** Opsi untuk melihat data tabular yang telah difilter.

---

### 💡 Insight Kunci yang Ditemukan

Dari analisis data yang mendalam, beberapa temuan kunci berhasil diidentifikasi:

1.  **Jarak adalah Faktor #1:** Jarak pengiriman memiliki korelasi positif terkuat dengan waktu pengiriman.
2.  **Rintangan Terbesar:** Lalu lintas padat (`High`) dan cuaca bersalju (`Snowy`) adalah dua kondisi eksternal yang paling signifikan memperlambat pengiriman.
3.  **Efek Interaksi:** Dampak cuaca bersalju menjadi **jauh lebih parah** ketika terjadi bersamaan dengan lalu lintas padat.
4.  **Temuan Mengejutkan:** Tipe kendaraan dan pengalaman kurir ternyata **tidak memiliki pengaruh yang signifikan** terhadap durasi pengiriman.
5.  **Profil Pengiriman Berisiko:** Kasus keterlambatan ekstrem (outlier) cenderung terjadi pada pengiriman **jarak jauh**, di **malam hari**, dan saat **cuaca hujan**.

---

### 🛠️ Teknologi yang Digunakan

- **Bahasa:** Python
- **Analisis Data:** Pandas
- **Visualisasi Data:** Plotly Express
- **Dashboard Framework:** Streamlit
