import streamlit as st

from app.api_handler.stock_data import get_stock_data

st.title("Sustainable Investment Dashboard")

ticker = st.text_input("Enter a stock ticker (e.g., AAPL):")
if ticker:
    data = get_stock_data(ticker)
    st.write(f"Displaying data for {ticker}:")
    st.dataframe(data)
