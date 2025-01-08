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

    # Main function for Streamlit app
    def main():
        # Inject custom CSS for full-width iframe
        custom_css = """
        <style>
            .main iframe {
                width: 100% !important;
                height: calc(100vh - 2rem) !important;
                border: none !important;
            }
            .main > div {
                padding: 0 !important;
            }
        </style>
        """
        st.markdown(custom_css, unsafe_allow_html=True)
    
        # Load and preprocess data
        data = load_data(csv_url)
        if data is not None:
            processed_data = preprocess_data(data)
            returns, nifty50 = calculate_returns(processed_data)
    
            # Filter for overlapping dates
            returns, nifty50 = filter_data_by_date(returns, nifty50)
    
            # Handle NaN and Inf values
            returns = returns.replace([np.inf, -np.inf], 0).fillna(0)
            nifty50 = nifty50.replace([np.inf, -np.inf], 0).fillna(0)
    
            # Generate QuantStats report
            try:
                qs.reports.html(returns, nifty50, output="report.html")
                with open("report.html", "r") as f:
                    report_html = f.read()
    
                # Embed the QuantStats report in full width
                st.components.v1.html(report_html, scrolling=True)
            except Exception as e:
                st.error(f"Error displaying QuantStats report: {e}")
if __name__ == "__main__":
    main()
