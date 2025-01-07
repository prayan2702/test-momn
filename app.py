import streamlit as st
from momn_streamlit_app import main as momn_main
from Strategy_performance import main as strategy_main
from strategy_tearsheet import main as tearsheet_main

# यह पहली Streamlit कमांड होनी चाहिए
st.set_page_config(page_title="Portfolio Report", layout="wide")

# यह पहली Streamlit कमांड होनी चाहिए
st.set_page_config(page_title="Portfolio Report", layout="wide")

# Modified CSS to fix the cutoff
hide_streamlit_style = """
    <style>
    div[data-testid="stSidebarNav"] {display: none !important;}
    div[data-testid="stHeader"] {display: none !important;}
    div.block-container {padding-top: 0rem !important; padding-bottom: 0rem !important;}
    section.main > div:has(~ footer ) {padding-top: 0rem !important;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# नेविगेशन टैब
tab1, tab2, tab3 = st.tabs(["Momentum App", "Strategy Performance", "Strategy Tearsheet"])

# प्रत्येक टैब के लिए सामग्री
with tab1:
    momn_main()

with tab2:
    strategy_main()

with tab3:
    tearsheet_main()

# नेविगेशन टैब
tab1, tab2, tab3 = st.tabs(["Momentum App", "Strategy Performance", "Strategy Tearsheet"])

# प्रत्येक टैब के लिए सामग्री
with tab1:
    momn_main()

with tab2:
    strategy_main()

with tab3:
    tearsheet_main()
