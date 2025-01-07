import streamlit as st
from momn_streamlit_app import main as momn_main
from Strategy_performance import main as strategy_main
from strategy_tearsheet import main as tearsheet_main

# Set the page layout (using wide layout for the page)
st.set_page_config(page_title="Portfolio Report", layout="wide")

# Sidebar with an option to show/hide
show_sidebar = st.sidebar.checkbox("Show Sidebar", value=True)

# If the checkbox is selected, display the sidebar
if show_sidebar:
    with st.sidebar:
        st.title("Navigation")
        option = st.radio(
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
        st.title("Strategy Tearsheet")
        try:
            tearsheet_main()
        except Exception as e:
            st.error(f"Error loading Strategy Tearsheet: {e}")

else:
    # When the sidebar is hidden, show full page content
    st.title("Full Page Content")
    st.write("Select 'Show Sidebar' to enable the sidebar navigation.")
