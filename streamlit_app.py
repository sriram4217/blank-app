import streamlit as st
import requests

st.title("💸 Crypto Price Checker (INR)")

crypto = st.text_input("Enter cryptocurrency (e.g. bitcoin, ethereum)")

if crypto:
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto.lower()}&vs_currencies=inr"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        price = data.get(crypto.lower(), {}).get("inr")
        if price:
            st.success(f"💰 {crypto.title()} price: ₹{price}")
        else:
            st.error("Crypto not found.")
    else:
        st.error("Failed to fetch data.")
