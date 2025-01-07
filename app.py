import streamlit as st
from momn_streamlit_app import main as momn_main
from Strategy_performance import main as strategy_main
from strategy_tearsheet import main as tearsheet_main

# Set the page layout (use wide layout for full page)
st.set_page_config(page_title="Portfolio Report", layout="wide")

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

# CSS to hide sidebar content (only remove content when option is selected)
if option != "Momentum App":  # Hide sidebar content when an option is selected
    st.sidebar.empty()  # This clears the content of the sidebar, but sidebar is still visible

# Optional: Custom CSS to ensure content is displayed in full width
full_width_css = """
    <style>
    /* Hide sidebar header but keep it visible */
    [data-testid="stSidebar"] {
        width: 0px;
        height: 0px;
    }
    div.block-container {
        margin-left: 0 !important;
    }
    </style>
"""
st.markdown(full_width_css, unsafe_allow_html=True)
