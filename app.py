import streamlit as st
from momn_streamlit_app import main as momn_main
from Strategy_performance import main as strategy_main
from strategy_tearsheet import main as tearsheet_main

# # Set page configuration to wide layout (this must be the first Streamlit command)
# st.set_page_config(page_title="Portfolio Report", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
pages = {
    "Momentum App": momn_main,
    "Strategy Performance": strategy_main,
    "Strategy Tearsheet": tearsheet_main
}

# Default Page
default_page = "Momentum App"
page = st.sidebar.radio("Go to", list(pages.keys()), index=0)

# Render Selected Page
pages[page]()
