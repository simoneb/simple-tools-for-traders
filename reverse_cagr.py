import streamlit as st
import pandas as pd

with st.form("reverse_cagr"):
    st.subheader("Calculate Reverse CAGR")
    st.write('Calculate the future value of your capital if it grows at a specified CAGR.')
    initialCapital = st.number_input("Initial capital", value=1000)
    cagr = st.number_input("CAGR %", value=10)
    periods = st.number_input("Periods (monts/years)", value=5)

    submitted = st.form_submit_button("Calculate")

    if submitted:
        endingCapital = initialCapital * pow(1 + cagr / 100, periods)
        st.write(f"Future value: {round(endingCapital)}")

        growth = pd.DataFrame(
            [(period, initialCapital := initialCapital * (1 + cagr / 100)) for period in range(1, periods + 1)],
            columns=["period", "value"])
        
        growth.value = round(growth.value)
        
        st.write("Growth Table")
        st.dataframe(growth, hide_index=True)
        st.write("Compounded growth chart")
        st.bar_chart(growth, x="period", y="value")

