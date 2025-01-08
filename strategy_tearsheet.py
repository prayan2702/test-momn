import streamlit as st
import pandas as pd
import numpy as np
import quantstats as qs


def main():
    st.title("Strategy Tearsheet")

    csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTuyGRVZuafIk2s7moScIn5PAUcPYEyYIOOYJj54RXYUeugWmOP0iIToljSEMhHrg_Zp8Vab6YvBJDV/pub?output=csv"

    @st.cache_data(ttl=0)
    def load_data(csv_url):
        try:
            data = pd.read_csv(csv_url)
            return data
        except Exception as e:
            st.error(f"An error occurred: {e}")
            return None

    def preprocess_data(data):
        rows_to_delete = data[
            data["Date"].isin(["Portfolio Value", "Absolute Gain", "Nifty50", "Day Change"])
        ].index
        data.drop(rows_to_delete, inplace=True)
        data = data.dropna(subset=["NAV"])
        data["Date"] = pd.to_datetime(data["Date"], format="%d-%b-%y")
        data = data.sort_values(by="Date")
        data["Date"] = data["Date"].apply(lambda x: x.replace(tzinfo=None))
        data.set_index("Date", inplace=True)
        data["NAV"] = pd.to_numeric(data["NAV"])
        data["Nifty50 Change %"] = (
            data["Nifty50 Change %"].str.rstrip("%").astype("float") / 100
        )
        data["Nifty50 NAV"] = (1 + data["Nifty50 Change %"]).cumprod()
        return data

    def calculate_returns(data):
        returns = data["NAV"].pct_change().dropna()
        nifty50 = data["Nifty50 Change %"].dropna()
        return returns, nifty50

    def filter_data_by_date(returns, nifty50):
        start_date = max(returns.index.min(), nifty50.index.min())
        end_date = min(returns.index.max(), nifty50.index.max())
        returns = returns[start_date:end_date]
        nifty50 = nifty50[start_date:end_date]
        return returns, nifty50

    data = load_data(csv_url)

    if data is not None:
        data = preprocess_data(data)
        returns, nifty50 = calculate_returns(data)
        returns, nifty50 = filter_data_by_date(returns, nifty50)
        qs.extend_pandas()
        st.subheader("Tearsheet")
        st.pyplot(qs.reports.html(returns, benchmark=nifty50, output=False))


if __name__ == "__main__":
    main()
