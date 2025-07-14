import requests
import pandas as pd
import streamlit as st

def fetch_data(url):
    try:
        response = requests.get(url)
        # Check if the request was successful
        response.raise_for_status()
        return response.text  # or response.json() if the response is in JSON format
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def write_to_file(data,filename):
    try:
        with open(filename, 'w') as file:
            file.write(data)
        return 'Done'
    except IOError as e:
        print(f"An error occurred while reading from file: {e}")
        return None
    
def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except IOError as e:
        print(f"An error occurred while reading from file: {e}")
        return None

def data_processing(raw_data):
    raw_data = raw_data.split("\n")
    data = list()
    for i in raw_data:
        if ';' in i:
            data.append(i)
        else:
            continue
    else:
        data = data[1:]

    ds = {'Scheme Code':[],'ISIN Div Payout/ ISIN Growth':[],'ISIN Div Reinvestment':[],'Scheme Name':[],'Net Asset Value':[],'Date':[]}

    for i in data:
        r = i.split(';')
        ds['Scheme Code'].append(r[0])
        ds['ISIN Div Payout/ ISIN Growth'].append(r[1])
        ds['ISIN Div Reinvestment'].append(r[2])
        ds['Scheme Name'].append(r[3])
        ds['Net Asset Value'].append(r[4])
        ds['Date'].append(r[5])
    else:
        df = pd.DataFrame(ds)
    return df

def program_start():
    filename = 'data.txt'
    url = 'https://www.amfiindia.com/spages/NAVAll.txt'
    data = fetch_data(url)
    if data:
        write_to_file(data,filename)
    raw_data = read_from_file(filename)

    df = data_processing(raw_data)
    return df

# Streamlit app
st.set_page_config(layout="wide")
st.title('Live Stock Price App')

k = program_start()
st.dataframe(k)
