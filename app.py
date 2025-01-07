import streamlit as st
from momn_streamlit_app import main as momn_main
from Strategy_performance import main as strategy_main
from strategy_tearsheet import main as tearsheet_main

# Set page configuration to wide layout (this must be the first Streamlit command)
st.set_page_config(page_title="Portfolio Report", layout="wide")

# Modified CSS to fix the cutoff
hide_streamlit_style = """
    <style>
    div[data-testid="stSidebarNav"] {display: none !important;}
    div[data-testid="stHeader"] {display: none !important;}
    div.block-container {padding-top: 0rem !important; padding-bottom: 0rem !important;}
    section.main > div:has(~ footer ) {padding-top: 0rem !important;}
    .st-emotion-cache-z5fcl4 {position: relative; top: -62px;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Session state for current page
if "current_page" not in st.session_state:
    st.session_state.current_page = "Momentum App"

# Navigation tabs
tab1, tab2, tab3 = st.tabs(["Momentum App", "Strategy Performance", "Strategy Tearsheet"])

# Tab click handling
if tab1:
    st.session_state.current_page = "Momentum App"
if tab2:
    st.session_state.current_page = "Strategy Performance"
if tab3:
    st.session_state.current_page = "Strategy Tearsheet"

# Load the selected page
if st.session_state.current_page == "Momentum App":
    momn_main()
elif st.session_state.current_page == "Strategy Performance":
    strategy_main()
elif st.session_state.current_page == "Strategy Tearsheet":
    tearsheet_main()
