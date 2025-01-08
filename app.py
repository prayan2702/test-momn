import streamlit as st
from momn_streamlit_app import main as momn_main
from Strategy_performance import main as strategy_main
from strategy_tearsheet import main as tearsheet_main

# Hardcoded username and password for login
USERNAME = "admin"
PASSWORD = "password123"

# Main application logic
def main():
    # Initialize session state for login
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    # Check if user is logged in
    if not st.session_state["logged_in"]:
        # Set default layout for login page
        st.set_page_config(page_title="Portfolio Report", layout="centered")
        login()
    else:
        # Set wide layout for the main app
        st.set_page_config(page_title="Portfolio Report", layout="wide")
        app_content()

# Function to handle login
def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state["logged_in"] = True
            st.experimental_rerun()  # Reload app to apply wide layout
        else:
            st.error("Invalid username or password")

# Function to handle logout
def logout():
    st.session_state["logged_in"] = False
    st.experimental_rerun()  # Reload app to reset login state

# Function to display main app content
def app_content():
    # Sidebar logout button
    st.sidebar.button("Logout", on_click=logout)

    # Sidebar with navigation
    option = st.sidebar.radio(
        "Go to:",
        ("Momentum App", "Strategy Performance", "Strategy Tearsheet"),
        index=0
    )

    # Content based on selected option
    if option == "Momentum App":
        st.title("Momentum App")
        try:
            momn_main()
        except Exception as e:
            st.error(f"Error loading Momentum App: {e}")

    elif option == "Strategy Performance":
        st.title("Strategy Performance")
        try:
            strategy_main()
        except Exception as e:
            st.error(f"Error loading Strategy Performance: {e}")

    elif option == "Strategy Tearsheet":
        try:
            tearsheet_main()
        except Exception as e:
            st.error(f"Error loading Strategy Tearsheet: {e}")

if __name__ == "__main__":
    main()
