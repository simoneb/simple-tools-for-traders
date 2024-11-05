import streamlit as st
import pandas as pd

def calculate_cagr(initial, ending, periods):
    return pow(ending / initial, 1 / periods) - 1

with st.form("cagr"):
    st.subheader("Calculate CAGR")
    st.write('Calculate the Compound Annual Growth Rate based on initial and ending capital.')
    initialCapital = st.number_input("Initial capital", value=1000)
    endingCapital = st.number_input("Ending capital", value=10000)
    periods = st.number_input("Periods (monts/years)", value=5)

    submitted = st.form_submit_button("Calculate")

    if submitted:
        cagr = calculate_cagr(initialCapital, endingCapital, periods)
        st.write(f"CAGR: {round(cagr * 100, 2)}%")
        
        growth = pd.DataFrame(
            [(period, initialCapital := initialCapital * (1 + cagr)) for period in range(1, periods + 1)],
            columns=["period", "value"])
        
        growth.value = round(growth.value)
        
        st.write("Growth Table")
        st.dataframe(growth, hide_index=True)
        st.write("Compounded growth chart")
        st.bar_chart(growth, x="period", y="value")

        
