import streamlit as st
from momn_streamlit_app import main as momn_main
from Strategy_performance import main as strategy_main
from strategy_tearsheet import main as tearsheet_main

# Set the page layout to wide
st.set_page_config(page_title="Portfolio Report", layout="wide")

# Adjust CSS to fix layout cutoff issue
fix_layout_style = """
    <style>
    div.block-container {
        padding-top: 6rem !important; /* Adjust padding to move content down */
        padding-bottom: 1rem !important;
    }
    section.main {
        margin-top: 3rem !important; /* Additional margin to ensure proper spacing */
    }
    header, footer {visibility: hidden;} /* Hide unnecessary header/footer */
    </style>
    """
st.markdown(fix_layout_style, unsafe_allow_html=True)

# Navigation Tabs
tab1, tab2, tab3 = st.tabs(["Momentum App", "Strategy Performance", "Strategy Tearsheet"])

# Content for each tab
with tab1:
    try:
        momn_main()
    except Exception as e:
        st.error(f"Error loading Momentum App: {e}")

with tab2:
    try:
        strategy_main()
    except Exception as e:
        st.error(f"Error loading Strategy Performance: {e}")

with tab3:
    try:
        tearsheet_main()
    except Exception as e:
        st.error(f"Error loading Strategy Tearsheet: {e}")
