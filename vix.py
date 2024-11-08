import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

st.subheader("VIX Term Structure")

df = pd.concat([
    yf.Ticker("%5EVXIND1").history('1d'),
    yf.Ticker("%5EVXIND2").history('1d'), 
    yf.Ticker("%5EVXIND3").history('1d')   
]) 
df['Name'] = ['vx1', 'vx2', 'vx3']

fig, ax = plt.subplots()
ax.plot(df.Name, df.Close)

st.pyplot(fig)

st.write(df)