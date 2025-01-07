import streamlit as st
from momn_streamlit_app import main as momn_main
from Strategy_performance import main as strategy_main
from strategy_tearsheet import main as tearsheet_main

# Set page configuration to wide layout (this must be the first Streamlit command)
st.set_page_config(page_title="Portfolio Report", layout="wide")

# नेविगेशन टैब
tab1, tab2, tab3 = st.tabs(["Momentum App", "Strategy Performance", "Strategy Tearsheet"])

# प्रत्येक टैब के लिए सामग्री
with tab1:
    momn_main()

with tab2:
    strategy_main()

with tab3:
    tearsheet_main()
