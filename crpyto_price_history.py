import streamlit as st
from cryptocmd import CmcScraper
import plotly.express as px
from datetime import datetime
st.write("# 비트코인 BTC 데이터")

st.sidebar.header('Menu')

name = st.sidebar.selectbox('Name', ['BTC', 'ETH', 'USDT'])

start_date = st.sidebar.date_input('Start date', datetime(2021, 1, 1))
end_date = st.sidebar.date_input('end_date', datetime(2021, 2, 18))

scraper = CmcScraper(name, start_date.strftime('%d-%m-%Y'), end_date.strftime('%d-%m-%Y'))
df = scraper.get_dataframe()

fig_close = px.line(df, x='Date', y=['Open', 'High', 'Low', 'Close'], title='가격')
fig_volume = px.line(df, x='Date', y=['Volume'], title='거래량')

st.plotly_chart(fig_close)
st.plotly_chart(fig_volume)