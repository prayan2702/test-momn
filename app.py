import streamlit as st
from momn_streamlit_app import main as momn_main
from Strategy_performance import main as strategy_main
from strategy_tearsheet import main as tearsheet_main

# Set the page layout
st.set_page_config(page_title="Portfolio Report", layout="wide")

# Custom CSS and JavaScript for hideable sidebar
hideable_sidebar_css = """
    <style>
    /* Hide sidebar by default */
    [data-testid="stSidebar"][aria-expanded="false"] {
        margin-left: -300px; /* Shift sidebar out of view */
    }

    /* Show sidebar when expanded */
    [data-testid="stSidebar"][aria-expanded="true"] {
        margin-left: 0; /* Bring sidebar into view */
    }

    /* Custom button to toggle sidebar */
    .sidebar-toggle {
        position: fixed;
        top: 1rem;
        left: 1rem;
        z-index: 1000;
        background-color: #007bff;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        cursor: pointer;
    }
    </style>

    <script>
    // JavaScript to toggle sidebar visibility and hide on option select
    document.addEventListener("DOMContentLoaded", function() {
        const toggleButton = document.querySelector('.sidebar-toggle');
        const sidebar = document.querySelector('[data-testid="stSidebar"]');

        // Toggle button functionality
        toggleButton.addEventListener('click', () => {
            const isExpanded = sidebar.getAttribute('aria-expanded') === "true";
            sidebar.setAttribute('aria-expanded', !isExpanded);
        });

        // Auto-hide sidebar when an option is selected
        const radioOptions = document.querySelectorAll('div[data-testid="stSidebar"] input[type="radio"]');
        radioOptions.forEach((option) => {
            option.addEventListener('change', () => {
                sidebar.setAttribute('aria-expanded', "false");
            });
        });
    });
    </script>
"""

# Add the CSS and JS for the sidebar toggle
st.markdown(hideable_sidebar_css, unsafe_allow_html=True)

# Add a toggle button to the main page
st.markdown('<div class="sidebar-toggle">☰ Menu</div>', unsafe_allow_html=True)

# Sidebar navigation menu
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
