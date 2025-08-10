# Mengimpor library yang dibutuhkan untuk aplikasi
import streamlit as st
import pandas as pd
import plotly.express as px


# Konfigurasi Halaman & Fungsi

# Mengatur layout halaman Streamlit
st.set_page_config(layout="wide")


# Muat data
@st.cache_data
def load_data(path):
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        st.error(f"File tidak ditemukan di path: {path}. Pastikan file ada di folder 'data/'.")
        return None
    

df = load_data('data/cleaned_food_delivery.csv')

# Membuat filter multiselect untuk Kondisi Cuaca
weather_options = st.sidebar.multiselect(
    "Pilih Kondisi Cuaca:",
    options=df['Weather'].unique(),
    default=df['Weather'].unique() # Defaultnya memilih semua opsi
)

# Membuat filter multiselect untuk Tingkat Lalu Lintas
traffic_options = st.sidebar.multiselect(
    "Pilih Kondisi Lalu Lintas:",
    options=df['Traffic_Level'].unique(),
    default=df['Traffic_Level'].unique() # Defaultnya memilih semua opsi
)

# Menerapkan filter ke DataFrame utama
# Hanya baris yang memenuhi kedua kondisi filter yang akan dipilih
df_filtered = df[df['Weather'].isin(weather_options) & df['Traffic_Level'].isin(traffic_options)]


# --- Halaman Utama ---
st.title("Dashboard Analisis Waktu Pengiriman Makanan 🚚")
st.markdown("Dashboard ini menyajikan analisis mendalam mengenai faktor-faktor yang memengaruhi waktu pengiriman.")


# --- Menampilkan Metrik Utama (KPIs) ---
st.markdown("### Metrik Utama")
total_deliveries = df_filtered.shape[0]
avg_delivery_time = df_filtered['Delivery_Time_min'].mean()
avg_distance = df_filtered['Distance_km'].mean()


# Menggunakan kolom untuk menata metrik agar rapi
col1, col2, col3 = st.columns(3)
col1.metric("Total Pengiriman", f"{total_deliveries}")
col2.metric("Rata-rata Waktu Kirim (menit)", f"{avg_delivery_time:.2f}")
col3.metric("Rata-rata Jarak (km)", f"{avg_distance:.2f}")

st.markdown("---")

# --- Baris 1: Scatter Plot & Box Plot ---
row1_col1, row1_col2 = st.columns([2, 1]) # Kolom pertama lebih lebar

with row1_col1:
    st.subheader("Jarak vs. Waktu Pengiriman")
    # Membuat scatter plot dengan Plotly Express
    fig_scatter = px.scatter(
        df_filtered,
        x='Distance_km',
        y='Delivery_Time_min',
        title='Hubungan Jarak dengan Waktu Pengiriman',
        labels={'Distance_km': 'Jarak (km)', 'Delivery_Time_min': 'Waktu Pengiriman (menit)'},
        trendline="ols", # Menambahkan garis tren regresi
        trendline_color_override="red"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

with row1_col2:
    st.subheader("Pengaruh Lalu Lintas")
    # Membuat box plot dengan Plotly Express
    fig_box_traffic = px.box(
        df_filtered,
        x='Traffic_Level',
        y='Delivery_Time_min',
        title='Distribusi Waktu Kirim per Tingkat Lalu Lintas',
        labels={'Traffic_Level': 'Tingkat Lalu Lintas', 'Delivery_Time_min': 'Waktu Pengiriman (menit)'},
        category_orders={"Traffic_Level": ["Low", "Medium", "High"]} # Mengurutkan sumbu x
    )
    st.plotly_chart(fig_box_traffic, use_container_width=True)
    
    
# --- Baris 2: Box Plot & Bar Plot Interaksi ---
row2_col1, row2_col2 = st.columns([1, 2]) # Kolom kedua lebih lebar

with row2_col1:
    st.subheader("Pengaruh Cuaca")
    # Membuat box plot untuk cuaca
    fig_box_weather = px.box(
        df_filtered,
        x='Weather',
        y='Delivery_Time_min',
        title='Distribusi Waktu Kirim per Kondisi Cuaca',
        labels={'Weather': 'Kondisi Cuaca', 'Delivery_Time_min': 'Waktu Pengiriman (menit)'}
    )
    st.plotly_chart(fig_box_weather, use_container_width=True)

with row2_col2:
    st.subheader("Kombinasi Paling Berisiko")
    # Membuat bar plot untuk interaksi lalu lintas dan cuaca
    # Kita perlu mengelompokkan data terlebih dahulu untuk mendapatkan rata-rata
    df_grouped = df_filtered.groupby(['Traffic_Level', 'Weather'])['Delivery_Time_min'].mean().reset_index()
    fig_bar_interaction = px.bar(
        df_grouped,
        x='Traffic_Level',
        y='Delivery_Time_min',
        color='Weather',
        title='Rata-rata Waktu Kirim: Interaksi Lalu Lintas & Cuaca',
        labels={'Traffic_Level': 'Tingkat Lalu Lintas', 'Delivery_Time_min': 'Rata-rata Waktu Pengiriman (menit)'},
        category_orders={"Traffic_Level": ["Low", "Medium", "High"]},
        barmode='group' # Mengelompokkan bar
    )
    st.plotly_chart(fig_bar_interaction, use_container_width=True)

# --- Menampilkan Data Mentah ---
st.markdown("---")
if st.checkbox("Tampilkan Data Mentah (setelah difilter)"):
    st.write(df_filtered)