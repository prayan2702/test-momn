import streamlit as st
import pandas as pd
import numpy as np
import quantstats as qs


def main():
    st.title("Tearsheet")

    # Replace with your published CSV link
    csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTuyGRVZuafIk2s7moScIn5PAUcPYEyYIOOYJj54RXYUeugWmOP0iIToljSEMhHrg_Zp8Vab6YvBJDV/pub?output=csv"

    # Load the data into a Pandas DataFrame
    @st.cache_data(ttl=0)  # Caching har baar bypass hoga
    def load_data(csv_url):
        try:
            data = pd.read_csv(csv_url)
            return data
        except Exception as e:
            st.error(f"An error occurred: {e}")
            return None

    # Data cleaning and preprocessing
    def preprocess_data(data):
        # Remove unwanted rows
        rows_to_delete = data[
            data["Date"].isin(["Portfolio Value", "Absolute Gain", "Nifty50", "Day Change"])
        ].index
        data.drop(rows_to_delete, inplace=True)

        # Remove rows without NAV
        data = data.dropna(subset=["NAV"])

        # Convert Date to datetime and remove timezone
        data["Date"] = pd.to_datetime(data["Date"], format="%d-%b-%y")
        data = data.sort_values(by="Date")
        data["Date"] = data["Date"].apply(lambda x: x.replace(tzinfo=None))  # Remove tz awareness
        data.set_index("Date", inplace=True)

        # Convert columns to numeric
        data["NAV"] = pd.to_numeric(data["NAV"])
        data["Nifty50 Change %"] = (
            data["Nifty50 Change %"].str.rstrip("%").astype("float") / 100
        )

        # Calculate Nifty50 NAV as a benchmark
        data["Nifty50 NAV"] = (1 + data["Nifty50 Change %"]).cumprod()

        return data

    # Calculate the daily returns
    def calculate_returns(data):
        returns = data["NAV"].pct_change().dropna()
        nifty50 = data["Nifty50 Change %"].dropna()
        return returns, nifty50

    # Filter data to ensure overlapping date ranges
    def filter_data_by_date(returns, nifty50):
        start_date = max(returns.index.min(), nifty50.index.min())
        end_date = min(returns.index.max(), nifty50.index.max())

        returns = returns[start_date:end_date]
        nifty50 = nifty50[start_date:end_date]

        return returns, nifty50

    # Load data
    data = load_data(csv_url)

    if data is not None:
        # Preprocess data
        data = preprocess_data(data)

        # Calculate returns
        returns, nifty50 = calculate_returns(data)

        # Filter data by date
        returns, nifty50 = filter_data_by_date(returns, nifty50)

        # Set QuantStats configuration
        qs.extend_pandas()

        # Display Tearsheet
        st.subheader("Tearsheet")
        st.pyplot(qs.reports.html(returns, benchmark=nifty50, output=False))

if __name__ == "__main__":
    main()
