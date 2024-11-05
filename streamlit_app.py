import streamlit as st

pages = {
    "Simple tools for traders": [],
    "CAGR": [
        st.Page("cagr.py", title="Calculate CAGR"),
        st.Page("reverse_cagr.py", title="Calculate reverse CAGR"),
    ],
    
}

st.header("Simple tools for traders", divider=True)
pg = st.navigation(pages)
pg.run()