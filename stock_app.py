import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

shown below are the stock closing prince and volume of Google

""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period = '1d', start = '2010-5-31', end = '2020-5-31')

st.write(
    """
## CLOSING PRICE
    """
)
st.line_chart(tickerDf.Close)
st.write(
    """
## VOLUME
    """
)

st.line_chart(tickerDf.Volume)