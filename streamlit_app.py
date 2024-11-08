import streamlit as st

pages = {
    "Simple tools for traders": [],
    "CAGR": [
        st.Page("cagr.py", title="Calculate CAGR"),
        st.Page("reverse_cagr.py", title="Calculate reverse CAGR"),
    ],
    "Minus": [
        st.Page('minus.py', title="Compensate minus")
    ],
    'VIX': [
        st.Page('vix.py', title="VIX Term Structure")
    ]
}

st.header("Simple tools for traders", divider=True)
pg = st.navigation(pages)
pg.run()