import pandas as pd
url = "https://raw.githubusercontent.com/nabxxmift23/submission/main/data/data%20bike_dicoding.csv"
df = pd.read_csv(url, sep = ';')

import streamlit as st
st.title('Analisis Usaha Rental Sepeda')
st.markdown(
    """
    Dashboard ini dibuat untuk menganalisis waktu dan kondisi yang tepat untuk melakukan usaha rental sepeda.
    """
)

st.header('Analisis Tren Bulanan Jumlah Rental Sepeda')
st.markdown(
    """
    Analisis ini bertujuan untuk melihat waktu yang tepat untuk melakukan rental sepeda berdasarkan bulan.
    """
)

import matplotlib.pyplot as plt

#data cleaning
df['dteday'] = pd.to_datetime(df['dteday'], format="%d/%m/%Y")
df['month'] = df['dteday'].dt.month
df['year'] = df['dteday'].dt.year

#Pertanyaan 1
cnt_bulanan = df.groupby(['year', 'month'])['cnt'].sum().reset_index()

st.subheader('Grafik Jumlah Rental Bikes per Bulan')

fig, ax = plt.subplots(figsize=(10, 4))
for year in cnt_bulanan['year'].unique():
    ax.plot(cnt_bulanan[cnt_bulanan['year'] == year]['month'], cnt_bulanan[cnt_bulanan['year'] == year]['cnt'],
             marker='o', linestyle='-', label=str(year))

ax.set_title('Jumlah Rental Bikes per Bulan')
ax.set_xlabel('Bulan')
ax.set_ylabel('Jumlah Rental Bikes')
ax.grid(True)
ax.legend()
st.pyplot(fig)
st.markdown(
    """
    Berdasarkan grafik di atas, dapat dilihat bahwa jumlah peminjaman sepeda cenderung naik pada rentang bulan Maret sampai dengan bulan September. Oleh karena itu, pemegang usaha yang melakukan bisnis rental sepeda disarankan untuk melakukan rental sepeda pada rentang waktu tersebut.
    """
)

#Pertanyaan 2
st.header('Analisis Korelasi antara Jumlah Rental Sepeda dengan Temperatur, Kelembapan Udara, dan Kecepatan Angin')

st.subheader('Grafik Korelasi Antara Temperatur dan Jumlah Rental Sepeda')
import seaborn as sns
fig, ax = plt.subplots()
sns.regplot(x=df['temp'], y=df['cnt'], ax=ax)
ax.set_title('Korelasi Antara Temperatur dan Jumlah Rental Bikes')
ax.set_xlabel('Temperatur (Normalized)')
ax.set_ylabel('Jumlah Rental Bikes')
st.pyplot(fig)

st.title('Korelasi Antara Kelembapan dan Jumlah Rental Bikes')
fig, ax = plt.subplots()
sns.regplot(x=df['hum'], y=df['cnt'], ax=ax)
ax.set_title('Korelasi Antara Kelembapan dan Jumlah Rental Bikes')
ax.set_xlabel('Kelembapan (Normalized)')
ax.set_ylabel('Jumlah Rental Bikes')
st.pyplot(fig)

st.title('Korelasi Antara Kecepatan Angin dan Jumlah Rental Bikes')
fig, ax = plt.subplots()
sns.regplot(x=df['windspeed'], y=df['cnt'], ax=ax)
ax.set_title('Korelasi Antara Kecepatan Angin dan Jumlah Rental Bikes')
ax.set_xlabel('Kecepatan Angin (Normalized)')
ax.set_ylabel('Jumlah Rental Bikes')
st.pyplot(fig)

st.markdown(
    """
    Temperatur dengan jumlah rental sepeda memiliki korelasi positif. Jika temperatur semakin tinggi, maka jumlah rental sepeda juga semakin banyak. Oleh karena itu, pemegang usaha bisa memperhatikan temperatur harian untuk menentukan waktu melakukan rental sepeda yang lebih baik, yaitu pada saat temperatur tinggi. Sementara itu, kelembapan dan kecepatan angin memiliki korelasi negatif dengan jumlah rental sepeda. Semakin tinggi kelembapan dan kecepatan angin, maka semakin sedikit jumlah rental sepeda. Oleh karena itu, pemegang usaha bisa memperhatikan kelembapan dan kecepatan angin harian untuk menentukan waktu melakukan rental sepeda yang lebih baik, yaitu pada saat kelembapan dan kecepatan angin harian rendah.
    """
)



