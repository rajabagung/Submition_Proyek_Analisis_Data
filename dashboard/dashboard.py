import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned hour data
hour_df = pd.read_csv("dashboard/cleaned_hour.csv")

# Title of the dashboard
st.title("Bike Sharing Data Dashboard")

# Visual 1: Impact of Weather on Total Bike Rentals
st.subheader("Pengaruh Cuaca terhadap Jumlah Total Penyewa Sepeda")
weather_rentals = hour_df.groupby('weathersit')['cnt'].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(data=weather_rentals, x='weathersit', y='cnt', palette='viridis')
plt.title('Total Penyewa Sepeda Berdasarkan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Jumlah Penyewa Sepeda')
plt.xticks(rotation=45)
st.pyplot(plt)

# Visual 2: Pattern of Bike Rentals by Hour of the Day
st.subheader("Pola Penyewaan Sepeda Berdasarkan Jam dalam Sehari")
plt.figure(figsize=(10, 5))
sns.lineplot(x='hr', y='cnt', data=hour_df, marker='o', color='blue')
plt.title("Jumlah Penyewa Sepeda per Jam")
plt.xlabel("Jam dalam Sehari")
plt.ylabel("Jumlah Penyewa")
st.pyplot(plt)

# Visual 3: Influence of Windspeed on Bike Rentals
st.subheader("Pengaruh Kecepatan Angin terhadap Jumlah Penyewa Sepeda")
plt.figure(figsize=(10, 5))
sns.scatterplot(x='windspeed', y='cnt', data=hour_df, alpha=0.5)
plt.title("Pengaruh Kecepatan Angin terhadap Jumlah Penyewa Sepeda")
plt.xlabel("Kecepatan Angin")
plt.ylabel("Jumlah Penyewa")
st.pyplot(plt)

# Visual 4: Significant Factors in Predicting Bike Rentals
st.subheader("Faktor Signifikan dalam Memprediksi Jumlah Penyewa Sepeda")
plt.figure(figsize=(10, 5))
correlation_matrix = hour_df.corr()
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', center=0)
plt.title("Heatmap Korelasi")
st.pyplot(plt)
