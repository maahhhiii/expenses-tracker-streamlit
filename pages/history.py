import streamlit as st
from database import get_data

st.title("📜 Transaction History")

df = get_data()

if df.empty:
    st.warning("No transactions found.")
else:
    st.dataframe(df, use_container_width=True)