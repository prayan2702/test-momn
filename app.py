import streamlit as st
from momn_streamlit_app import main as momn_main
from Strategy_performance import main as strategy_main
from strategy_tearsheet import main as tearsheet_main

# Hardcoded username and password for login
USERNAME = "prayan"
PASSWORD = "prayan"

# Set the page layout to wide
st.set_page_config(page_title="Portfolio Report", layout="wide")

# Function to handle login
def login():
    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])  # Centered layout
        with col2:
            st.title("Login Page")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.button("Login"):
                if username == USERNAME and password == PASSWORD:
                    st.session_state["logged_in"] = True
                    st.session_state["page"] = "Momentum App"  # Default page after login
                    st.rerun()
                else:
                    st.error("Invalid username or password")

# Function to handle logout
def logout():
    st.session_state["logged_in"] = False
    st.rerun()

# Sidebar Navigation (Dropdown)
def sidebar_navigation():
    st.sidebar.title("Quantified Self")

    # Dropdown to select page
    selected_page = st.sidebar.selectbox(
        "Select a Page",
        ["Momentum App", "Strategy Performance", "Strategy Tearsheet"],
        index=["Momentum App", "Strategy Performance", "Strategy Tearsheet"].index(st.session_state["page"])
    )

    # Update the current page on change
    if selected_page != st.session_state["page"]:
        st.session_state["page"] = selected_page
        st.rerun()

    # Sidebar logout button
    if st.sidebar.button("Logout"):
        logout()

# Function to display main app content
def app_content():
    sidebar_navigation()

    # Render content based on the selected page
    if st.session_state["page"] == "Momentum App":
        st.title("Momentum App")
        try:
            momn_main()
        except Exception as e:
            st.error(f"Error loading Momentum App: {e}")
    elif st.session_state["page"] == "Strategy Performance":
        st.title("Strategy Performance")
        try:
            strategy_main()
        except Exception as e:
            st.error(f"Error loading Strategy Performance: {e}")
    elif st.session_state["page"] == "Strategy Tearsheet":
        st.title("Strategy Tearsheet")
        try:
            tearsheet_main()
        except Exception as e:
            st.error(f"Error loading Strategy Tearsheet: {e}")

# Main application logic
def main():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    if "page" not in st.session_state:
        st.session_state["page"] = "Momentum App"

    if not st.session_state["logged_in"]:
        login()
    else:
        app_content()

if __name__ == "__main__":
    main()
