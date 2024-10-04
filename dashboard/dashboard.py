import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
hr_df = pd.read_csv('hour.csv')

# Data preprocessing
hr_df['dteday'] = pd.to_datetime(hr_df['dteday'])
hr_df['month'] = hr_df['dteday'].dt.month_name()
hr_df['hour'] = hr_df['hr']

# Set up the Streamlit app
st.title("Dashboard Penyewaan Sepeda")

# Sidebar for user input
st.sidebar.header("Filter")
selected_month = st.sidebar.selectbox("Pilih Bulan", hr_df['month'].unique())
selected_hour = st.sidebar.slider("Pilih Jam", min_value=0, max_value=23, value=(0, 23))

# Filter data based on selections
filtered_data = hr_df[(hr_df['month'] == selected_month) & (hr_df['hour'].between(selected_hour[0], selected_hour[1]))]

# Section: Pengaruh Cuaca terhadap Jumlah Penyewa Sepeda
st.header("Pengaruh Cuaca terhadap Jumlah Penyewa Sepeda")
weather_count = filtered_data.groupby('weather_cond')['count'].sum().reset_index()
st.bar_chart(weather_count.set_index('weather_cond'))

# Section: Pola Penyewaan Sepeda Berdasarkan Jam
st.header("Pola Penyewaan Sepeda Berdasarkan Jam dalam Sehari")
hourly_count = filtered_data.groupby('hour')['count'].sum().reset_index()
st.line_chart(hourly_count.set_index('hour'))

# Section: Pengaruh Kecepatan Angin
st.header("Pengaruh Kecepatan Angin terhadap Jumlah Penyewa Sepeda")
windspeed_count = filtered_data.groupby('windspeed')['count'].sum().reset_index()
st.scatter_chart(windspeed_count.set_index('windspeed'))

# Section: Faktor Signifikan dalam Memprediksi Jumlah Penyewa Sepeda
st.header("Matriks Korelasi")
correlation = hr_df.corr()
plt.figure(figsize=(10, 6))
sns.heatmap(correlation, annot=True, fmt=".2f", cmap='coolwarm')
st.pyplot(plt)

# Run the app
if __name__ == '__main__':
    st.run()
