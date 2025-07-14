# Mutual Fund & Stock Price Streamlit App

This project provides a Streamlit-based dashboard for viewing mutual fund NAVs and live stock prices, with data sourced from AMFI and Yahoo Finance APIs. It is designed for real-time financial analysis and visualization.

## Project Structure
- `mutual_fund.py`: Fetches mutual fund NAV data from AMFI, processes it, and displays it in a Streamlit app.
- `real_time_fund.py`: Displays live stock prices and top holdings for selected mutual funds using Yahoo Finance and YahooQuery APIs. Also loads fund codes from `codes.json`.
- `data.txt`: Contains sample mutual fund NAV data in a semicolon-separated format.
- `codes.json`: Stores mapping of scheme codes to fund names for lookup in the dashboard.

## Features
- Real-time NAV and stock price display.
- Data processing and visualization using Pandas and Streamlit.
- Lookup and display of top holdings for mutual funds.

## How to Run
1. Ensure Python 3.11+ and required packages are installed (see your environment's `lib/python3.11/site-packages`).
2. Run the Streamlit app:
   ```sh
   streamlit run mutual_fund.py
   # or
   streamlit run real_time_fund.py
   ```
3. Interact with the dashboard in your browser.

## Requirements
- Python 3.11+
- streamlit
- pandas
- requests
- yfinance
- yahooquery
- mftool

## Data Sources
- AMFI India NAV data: https://www.amfiindia.com/spages/NAVAll.txt
- Yahoo Finance APIs for live stock prices and holdings

## Notes
- The project is organized for easy extension to other mutual fund categories or additional analytics.
- Data files (`data.txt`, `codes.json`) should be kept up-to-date for best results.
