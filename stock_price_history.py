import streamlit as st
import pandas_datareader as pdr

st.write('''
# 삼성전자 주식 데이터
마감 가격과 거래량을 차트로 보여줍니다!
''')

df = pdr.get_data_yahoo('005930.KS', '2020-02-18', '2021-02-18')

st.line_chart(df.Close)
st.line_chart(df.Volume)