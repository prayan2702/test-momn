import streamlit as st
from momn_streamlit_app import main as momn_main
from Strategy_performance import main as strategy_main
from strategy_tearsheet import main as tearsheet_main

# Set page layout to wide for the overall app
st.set_page_config(page_title="Portfolio Report", layout="wide")

# Custom CSS to control layout per tab
custom_css = """
    <style>
    /* Default block container (applies to all tabs initially) */
    div.block-container {
        max-width: 1200px;
        margin: auto;
        padding: 2rem 1rem;
    }
    
    /* Wide layout for tabs 2 and 3 */
    body[data-tab="tab2"] div.block-container,
    body[data-tab="tab3"] div.block-container {
        max-width: 100%;
        padding: 2rem;
    }
    </style>
    <script>
    // JavaScript to add a custom class based on the active tab
    document.addEventListener('DOMContentLoaded', function () {
        let tabs = document.querySelectorAll('div[data-testid="stTabs"] button');
        tabs.forEach((tab, index) => {
            tab.addEventListener('click', () => {
                document.body.setAttribute('data-tab', 'tab' + (index + 1));
            });
        });
        // Set the initial tab on page load
        document.body.setAttribute('data-tab', 'tab1');
    });
    </script>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Define tabs
tab1, tab2, tab3 = st.tabs(["Momentum App", "Strategy Performance", "Strategy Tearsheet"])

# Content for each tab
with tab1:
    st.write("This is the centered layout for Tab 1.")
    try:
        momn_main()
    except Exception as e:
        st.error(f"Error loading Momentum App: {e}")

with tab2:
    st.write("This is the wide layout for Tab 2.")
    try:
        strategy_main()
    except Exception as e:
        st.error(f"Error loading Strategy Performance: {e}")

with tab3:
    st.write("This is the wide layout for Tab 3.")
    try:
        tearsheet_main()
    except Exception as e:
        st.error(f"Error loading Strategy Tearsheet: {e}")
