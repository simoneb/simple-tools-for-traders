import streamlit as st
import pandas as pd


with st.form("minus"):
    st.subheader("Compensate minus")
    st.write('This form allows you to calculate how much plus you must generate to compensate a certain amount of minus.')
    
    minusAmount = st.number_input("Minus amount", value=1000)
    capitalTax = st.number_input("Capital gain tax % of the asset you want to sell", value=26.0)
    profitFromStock = st.number_input('Total profit from asset you want to sell', value=None)
    quotes = st.number_input('Number of quotes you own of the asset you want to sell', value=None)

    submitted = st.form_submit_button("Calculate")

    if submitted:
        plus = minusAmount / (capitalTax / 100)
        st.write(f"You need to generate {round(plus)} plus to compensate the {minusAmount} minus")

        if profitFromStock and quotes:
            profitPerQuote = profitFromStock / quotes
            quotesToSell = plus / profitPerQuote
            st.write(f"You need to sell {round(quotesToSell)} quotes to compensate the minus")


        
        

        
