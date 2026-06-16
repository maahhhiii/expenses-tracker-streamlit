import streamlit as st
from database import get_data, update_data

st.title("✏️ Edit Transaction")

df = get_data()

if not df.empty:

    transaction_id = st.selectbox(
        "Select Transaction ID",
        df["id"]
    )

    selected_row = df[df["id"] == transaction_id].iloc[0]

    date = st.date_input(
        "Date",
        selected_row["date"]
    )

    category = st.text_input(
        "Category",
        selected_row["category"]
    )

    transaction_type = st.selectbox(
        "Type",
        ["Income", "Expenses"],
        index=0 if selected_row["type"] == "Income" else 1
    )

    amount = st.number_input(
        "Amount",
        value=float(selected_row["amount"])
    )

    if st.button("Update Transaction"):

        update_data(
            transaction_id,
            date,
            category,
            transaction_type,
            amount
        )

        st.success("Transaction updated successfully!")