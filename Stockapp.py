import yfinance as yf
import streamlit as st
import pandas as pd 

st.write(
    """
    ## Simple StockPrice App

    shown are the stock closing price and volume of Google !

    """)
tickerSymbol ="GOOGL"
tickerSymbol2="AAPL"

tickerData =yf.Ticker(tickerSymbol)

tickerDf=tickerData.history(period='1d', start='2010-5-31',end='2023-8-31')

st.write(
    """
    ### Closing Prices
    """
)

st.line_chart(tickerDf.Close)

st.write(
    """
    ### Google Volume prices
    """
)
st.line_chart(tickerDf.Volume)


st.write(
    """
    ### stock closing price and volume of Apple !

    """)

tickerData2 =yf.Ticker(tickerSymbol2)

tickerDf2=tickerData2.history(period='1d', start='2010-5-31',end='2023-8-31')

st.write(
    """
    ### Apple Closing Prices
    """
)
st.line_chart(tickerDf2.Close)

st.write(

"""
### Apple Volume  Prices 

"""
)
st.line_chart(tickerDf2.Volume)