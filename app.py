import streamlit as st
from database import get_data

st.set_page_config(
    page_title="Expenses Tracker",
    layout="wide",
    page_icon="💰"
)

st.title("💰 Expenses Tracker Dashboard")
st.markdown("---")

df = get_data()

if not df.empty:
    total_income = df[df["type"] == "Income"]["amount"].sum()
    total_expenses = df[df["type"] == "Expenses"]["amount"].sum()
else:
    total_income = 0
    total_expenses = 0

balance = total_income - total_expenses

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="💵 Total Income",
        value=f"${total_income:,.2f}"
    )

with col2:
    st.metric(
        label="💸 Total Expenses",
        value=f"${total_expenses:,.2f}"
    )

with col3:
    st.metric(
        label="🏦 Total Balance",
        value=f"${balance:,.2f}"
    )

st.markdown("---")

st.subheader("📋 Recent Transactions")

if df.empty:
    st.info("No transactions found.")
else:
    st.dataframe(df, use_container_width=True)