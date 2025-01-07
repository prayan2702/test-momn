import streamlit as st
from momn_streamlit_app import main as momn_main
from Strategy_performance import main as strategy_main
from strategy_tearsheet import main as tearsheet_main

# Set page configuration to wide layout (this must be the first Streamlit command)
st.set_page_config(page_title="Portfolio Report", layout="wide")


# CSS कोड
hide_streamlit_style = """
            <style>
            div[data-testid="stSidebarNav"] {display: none;}
            div.block-container {padding-top: 0rem;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# सत्र स्थिति में वर्तमान पृष्ठ
if "current_page" not in st.session_state:
    st.session_state.current_page = "Momentum App"

# नेविगेशन टैब
tab1, tab2, tab3 = st.tabs(["Momentum App", "Strategy Performance", "Strategy Tearsheet"])

# टैब 1 के लिए
if tab1:
    st.session_state.current_page = "Momentum App"
if tab2:
    st.session_state.current_page = "Strategy Performance"
if tab3:
    st.session_state.current_page = "Strategy Tearsheet"

# चयनित पृष्ठ लोड करें
if st.session_state.current_page == "Momentum App":
    momn_main()
elif st.session_state.current_page == "Strategy Performance":
    strategy_main()
elif st.session_state.current_page == "Strategy Tearsheet":
    tearsheet_main()
