import streamlit as st
from momn_streamlit_app import main as momn_main
from Strategy_performance import main as strategy_main
from strategy_tearsheet import main as tearsheet_main

# Hardcoded username and password for login
USERNAME = "prayan"
PASSWORD = "prayan"

# Set the page layout
st.set_page_config(page_title="Portfolio Report")

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
    # Sidebar navigation with clickable text
    with st.sidebar:
        pages = ["Momentum App", "Strategy Performance", "Strategy Tearsheet"]
        
        # Display pages with clickable links
        for page in pages:
            if st.session_state["page"] == page:
                st.markdown(f"**<div style='padding: 8px; background-color: #d0d7e2; border-radius: 5px; font-weight: bold;'>{page}</div>**", unsafe_allow_html=True)
            else:
                if st.markdown(f"<div style='padding: 8px; cursor: pointer;' onclick='window.location.reload();'>{page}</div>", unsafe_allow_html=True):
                    st.session_state["page"] = page
                    st.experimental_rerun()

        # Sidebar logout button
        if st.button("Logout"):
            logout()

    # Render content based on the selected page
    if st.session_state["page"] == "Momentum App":
        with st.container():
            col1, col2, col3 = st.columns([1, 2, 1])  # Centered layout
            with col2:
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
    # Initialize session state for login and navigation
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    if "page" not in st.session_state:
        st.session_state["page"] = "Momentum App"

    # Check if user is logged in
    if not st.session_state["logged_in"]:
        login()
    else:
        app_content()

if __name__ == "__main__":
    main()
