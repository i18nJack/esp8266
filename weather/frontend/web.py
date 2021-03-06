import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


file_name = 'data.csv'

def load_data():
    df = pd.read_csv(file_name)
    return df

st.markdown("<h1 style='text-align: center;'>IoT on ARMBIAN</h1>", unsafe_allow_html=True)
st.write('red: BMP280')
st.write('green: DHT11')

df = load_data()
df.time = pd.to_datetime(df.time)

fig, ax1 = plt.subplots(figsize=(13,8))

ax1.plot(df['time'], df['t1'], color='r', linewidth=3)
ax1.plot(df['time'], df['t2'], color='g', linewidth=3)
ax1.grid(True, linestyle='-.')

ax1.set_xlabel('Time', fontsize=18)

ax1.set_ylabel('Temperature / ℃', fontsize=18)
ax1.tick_params(axis='y')

ax1.yaxis.set_tick_params(labelsize=18)

#--------------------
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.plot(df['time'], df['humidity'], color=color, linewidth=2)

ax2.set_ylabel('Humidity / %', fontsize=18)
ax2.tick_params(axis='y')
ax2.yaxis.set_tick_params(labelsize=18)

locator = mdates.HourLocator(interval=2)
ax1.xaxis.set_major_locator(locator)
formatter = mdates.DateFormatter("%H")
ax1.xaxis.set_major_formatter(formatter)

fig.tight_layout()
st.pyplot(fig)