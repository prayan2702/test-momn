import streamlit as st
from momn_streamlit_app import main as momn_main
from Strategy_performance import main as strategy_main
from strategy_tearsheet import main as tearsheet_main

# Set the page layout
st.set_page_config(page_title="Portfolio Report", layout="wide")

# Hardcoded credentials
USERNAME = "prayan"
PASSWORD = "prayan"

# --- Login Form ---
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        if username == USERNAME and password == PASSWORD:
            st.session_state["logged_in"] = True
            st.rerun()
        else:
            st.error("Invalid username or password")

# --- Main App Content ---
if st.session_state["logged_in"]:
    st.sidebar.title("Navigation")

    pages = {
        "Momentum App": momn_main,
        "Strategy Performance": strategy_main,
        "Strategy Tearsheet": tearsheet_main
    }

    selection = st.sidebar.radio("Go to:", list(pages.keys()))

    # Call the selected page function
    pages[selection]()

    # Logout Button
    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.rerun()
