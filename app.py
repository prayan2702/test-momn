import streamlit as st
from momn_streamlit_app import main as momn_main
from Strategy_performance import main as strategy_main
from strategy_tearsheet import main as tearsheet_main

# Hardcoded username and password for login
USERNAME = "admin"
PASSWORD = "password123"

# Set the page layout (wide for the app)
st.set_page_config(page_title="Portfolio Report", layout="wide")

# Function to handle login
def login():
    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])  # Create centered layout for login
        with col2:
            st.title("Login Page")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.button("Login"):
                if username == USERNAME and password == PASSWORD:
                    st.session_state["logged_in"] = True
                    st.experimental_rerun()
                else:
                    st.error("Invalid username or password")

# Function to handle logout
def logout():
    st.session_state["logged_in"] = False
    st.experimental_rerun()

# Function to display main app content
def app_content():
    # Sidebar navigation as text-based links
    st.sidebar.title("Navigation")
    pages = {
        "Momentum App": "momentum",
        "Strategy Performance": "strategy_performance",
        "Strategy Tearsheet": "strategy_tearsheet"
    }
    selected_page = st.sidebar.radio("Select a page:", list(pages.keys()))

    # Sidebar logout button
    st.sidebar.button("Logout", on_click=logout)

    # Render content based on selected page
    if selected_page == "Momentum App":
        with st.container():
            col1, col2, col3 = st.columns([1, 2, 1])  # Centered layout
            with col2:
                st.title("Momentum App")
                try:
                    momn_main()
                except Exception as e:
                    st.error(f"Error loading Momentum App: {e}")
    elif selected_page == "Strategy Performance":
        st.title("Strategy Performance")
        try:
            strategy_main()
        except Exception as e:
            st.error(f"Error loading Strategy Performance: {e}")
    elif selected_page == "Strategy Tearsheet":
        st.title("Strategy Tearsheet")
        try:
            tearsheet_main()
        except Exception as e:
            st.error(f"Error loading Strategy Tearsheet: {e}")

# Main application logic
def main():
    # Initialize session state for login
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    # Check if user is logged in
    if not st.session_state["logged_in"]:
        login()
    else:
        app_content()

if __name__ == "__main__":
    main()
