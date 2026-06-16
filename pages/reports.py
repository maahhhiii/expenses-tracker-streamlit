import streamlit as st
import matplotlib.pyplot as plt
from database import get_data

st.title("📊 Reports")

df = get_data()

if not df.empty:

    total_income = df[df["type"] == "Income"]["amount"].sum()
    total_expenses = df[df["type"] == "Expenses"]["amount"].sum()

    labels = ["Income", "Expenses"]
    values = [total_income, total_expenses]

    fig, ax = plt.subplots()
    f = ax.pie(values, labels=labels, autopct="%1.1f%%")
    st.pyplot(fig,use_container_width=True)

else:
    st.info("No data available.")