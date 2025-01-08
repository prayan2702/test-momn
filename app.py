import streamlit as st
from momn_streamlit_app import main as momn_main
from Strategy_performance import main as strategy_main
from strategy_tearsheet import main as tearsheet_main

# Hardcoded username and password for login
USERNAME = "prayan"
PASSWORD = "prayan"

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
                    st.session_state["page"] = "Momentum App"  # Default page after login
                    st.experimental_rerun()
                else:
                    st.error("Invalid username or password")

# Function to handle logout
def logout():
    st.session_state["logged_in"] = False
    st.experimental_rerun()

# Function to display main app content
def app_content():
    # Sidebar with clickable text links
    st.sidebar.title("Navigation")
    st.sidebar.markdown(
        """
        <ul>
            <li><a href="?page=Momentum App">Momentum App</a></li>
            <li><a href="?page=Strategy Performance">Strategy Performance</a></li>
            <li><a href="?page=Strategy Tearsheet">Strategy Tearsheet</a></li>
        </ul>
        """,
        unsafe_allow_html=True,
    )
    # Sidebar logout button
    if st.sidebar.button("Logout"):
        logout()

    # Get current page from query parameters
    query_params = st.experimental_get_query_params()
    selected_page = query_params.get("page", ["Momentum App"])[0]

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
