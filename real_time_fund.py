import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mftool import Mftool
from yahooquery import Ticker
import json

# Function to load JSON data
def load_json(file_path = 'codes.json'):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def get_stock_price(symbol):
    # Fetch the stock data
    stock = yf.Ticker(symbol)
    
    # Get the live price
    data = stock.history(period='5d')  # Get historical data for the last day
    if not data.empty:
        prev_close_price = data['Close'].iloc[-2]  # Get the prev closing price
        latest_price = data['Close'].iloc[-1]  # Get the last closing price
        return prev_close_price,latest_price
    else:
        return None

# Streamlit app
st.title('Live Stock Price App')

# Input field for stock symbol
scheme_new_code = st.text_input('Enter New scheme code (e.g., 0P00011MAX, 117448):', '0P00011MAX')
json_data = load_json()
df = pd.DataFrame(list(json_data.items()), columns=['New Scheme Code', 'Fund Name'])
with st.expander("Click to Expand Table"):
    st.write("Here is a table of Schema Code and Schema Name:")
    st.dataframe(df)

if scheme_new_code:
    ticker = Ticker(scheme_new_code+'.BO')
    r = df[df['New Scheme Code'] == scheme_new_code]
    st.write("Top Holdings for ",scheme_new_code,' schema :', r['Fund Name'].values[0])
    holding = ticker.fund_top_holdings
    holding['Percent'] = holding['holdingPercent']*100
    holding = holding.drop('holdingPercent', axis=1)

    for i in holding.index:
        holding.loc[i, 'Prev'] = get_stock_price(holding['symbol'][i])[0]
        holding.loc[i, 'Latest'] = get_stock_price(holding['symbol'][i])[1]
        holding.loc[i, 'Change'] = 1 + (holding.loc[i, 'Latest'] - holding.loc[i, 'Prev']) / holding.loc[i, 'Prev']
        holding.loc[i, 'New_Percent'] = holding.loc[i, 'Change'] * holding.loc[i, 'Percent']
    st.write(holding)
    st.write(sum(holding['Percent']))
    st.write(sum(holding['New_Percent']))
        
