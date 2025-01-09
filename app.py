import streamlit as st
import streamlit_authenticator as stauth
from momn_streamlit_app import main as momn_main
from Strategy_performance import main as strategy_main
from strategy_tearsheet import main as tearsheet_main

# --- Load Credentials ---
credentials = {
    "usernames": {
        "prayan": {
            "name": "Prayan",
            "password": stauth.Hasher(["prayan"]).generate()
        }
    }
}

# --- Authenticator ---
authenticator = stauth.Authenticate(
    credentials,
    "portfolio_dashboard",  # Name of your cookie
    "abcdef",  # Cookie key
    cookie_expiry_days=30,  # Cookie expiration
)

# Set the page layout to wide
st.set_page_config(page_title="Portfolio Report", layout="wide")

# --- Main App Content ---

def main_app():
    # Sidebar Navigation with Clickable Text
    def sidebar_navigation():
        pages = ["Momentum App", "Strategy Performance", "Strategy Tearsheet"]
        for page in pages:
            if st.session_state["page"] == page:
                st.sidebar.write(f"**{page}**")
            else:
                if st.sidebar.button(page):
                    st.session_state["page"] = page
                    st.rerun()

    if "page" not in st.session_state:
      st.session_state["page"] = "Momentum App"

    sidebar_navigation()

    # --- Page Content ---
    if st.session_state["page"] == "Momentum App":
        momn_main()

    elif st.session_state["page"] == "Strategy Performance":
        strategy_main()

    elif st.session_state["page"] == "Strategy Tearsheet":
        tearsheet_main()
    

# --- Login Form ---
name, authentication_status, username = authenticator.login(
    "Login", "main"
)  # name, authentication status and username are returned

if authentication_status:
    authenticator.logout("Logout", "sidebar")
    main_app()
elif authentication_status == False:
    st.error("Username/password is incorrect")
elif authentication_status == None:
    st.warning("Please enter your username and password")
