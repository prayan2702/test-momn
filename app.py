import streamlit as st
from momn_streamlit_app import main as momn_main
from Strategy_performance import main as strategy_main
from strategy_tearsheet import main as tearsheet_main

# # यह पहली Streamlit कमांड होनी चाहिए
# st.set_page_config(page_title="Portfolio Report", layout="wide")

hide_streamlit_style = """
    <style>
    div[data-testid="stSidebarNav"] {display: none !important;}
    div[data-testid="stHeader"] {display: none !important;}
    div.block-container {
        padding-top: 2rem !important; /* Adjust top padding */
        padding-bottom: 0rem !important;
    }
    section.main > div:has(~ footer ) {
        padding-top: 2rem !important; /* Adjust main section's top padding */
    }
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# Navigation Tabs
tab1, tab2, tab3 = st.tabs(["Momentum App", "Strategy Performance", "Strategy Tearsheet"])

# Content for each tab
with tab1:
    try:
        momn_main()
    except Exception as e:
        st.error(f"Error loading Momentum App: {e}")

with tab2:
    try:
        strategy_main()
    except Exception as e:
        st.error(f"Error loading Strategy Performance: {e}")

with tab3:
    try:
        tearsheet_main()
    except Exception as e:
        st.error(f"Error loading Strategy Tearsheet: {e}")
