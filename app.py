import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Set up the style for seaborn plots
sns.set(style='whitegrid')

# Load data function
@st.cache_data
def load_data(filename):
    data = pd.read_csv(filename)
    return data

# Load your daily data
day_df = load_data('data/day.csv')

# Streamlit application title
st.title('Dashboard Analisis Permintaan Penyewaan Sepeda')

# Creating a sidebar for user inputs
st.sidebar.header('Filter Tanggal')

# Date filter configuration
min_date = pd.to_datetime(day_df['dteday']).min()
max_date = pd.to_datetime(day_df['dteday']).max()

start_date = st.sidebar.date_input('Tanggal Mulai', min_date)
end_date = st.sidebar.date_input('Tanggal Akhir', max_date)

# Filter the dataframe based on user selection
start_date = pd.Timestamp(start_date)
end_date = pd.Timestamp(end_date)

mask = (pd.to_datetime(day_df['dteday']) >= start_date) & (pd.to_datetime(day_df['dteday']) <= end_date)
filtered_day_df = day_df.loc[mask]


# Display filtered data
st.header('Data Penyewaan Sepeda Harian')
st.write(filtered_day_df)

# Visualizing Total Bike Rentals by Month
st.header('Total Penyewaan Sepeda per Bulan')

fig_month, ax_month = plt.subplots()
sns.barplot(data=filtered_day_df, x='mnth', y='cnt', ax=ax_month, estimator=sum, ci=None)
ax_month.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax_month.set_xlabel('Bulan')
ax_month.set_ylabel('Total Penyewaan Sepeda')
ax_month.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))  # Format y-axis as integers
st.pyplot(fig_month)

# Visualizing Total Bike Rentals by Weather Situation
st.header('Total Penyewaan Sepeda Berdasarkan Kondisi Cuaca')

fig_weather, ax_weather = plt.subplots()
sns.barplot(data=filtered_day_df, x='weathersit', y='cnt', ax=ax_weather, estimator=sum, ci=None)
ax_weather.set_xticklabels(['Cerah', 'Berkabut', 'Hujan', 'Cuaca Buruk'])
ax_weather.set_xlabel('Kondisi Cuaca')
ax_weather.set_ylabel('Total Penyewaan Sepeda')
ax_weather.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))  # Format y-axis as integers
st.pyplot(fig_weather)

# Footer
st.write('Dashboard dikembangkan menggunakan Streamlit')

# To run the Streamlit app, save this script as `app.py` and run using:
# streamlit run app.py