import streamlit as st
from database import add_data

st.title("➕ Add Transaction")

date = st.date_input("Date")

category = st.text_input("Category")

transaction_type = st.selectbox(
    "Type",
    ["Income", "Expenses"]
)

amount = st.number_input(
    "Amount",
    min_value=0.0
)

if st.button("Save Transaction"):
    add_data(
        date,
        category,
        transaction_type,
        amount
    )

    st.success("Transaction added successfully!")