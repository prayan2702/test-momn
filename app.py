import streamlit as st
from momn_streamlit_app import main as momn_main
from Strategy_performance import main as strategy_main
from strategy_tearsheet import main as tearsheet_main

# Hardcoded username and password for login
USERNAME = "prayan"
PASSWORD = "prayan"

# Set the page layout (use wide layout for full page)
st.set_page_config(page_title="Portfolio Report", layout="wide")

# Function to handle login
def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state["logged_in"] = True
            st.success("Logged in successfully!")
        else:
            st.error("Invalid username or password")

# Function to handle logout
def logout():
    st.session_state["logged_in"] = False
    st.success("Logged out successfully!")

# Main application logic
def main():
    # Initialize session state for login
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    # Check if user is logged in
    if not st.session_state["logged_in"]:
        login()
    else:
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
