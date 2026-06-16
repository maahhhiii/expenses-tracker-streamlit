import sqlite3
import pandas as pd

conn = sqlite3.connect("expenses.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    category TEXT,
    type TEXT,
    amount REAL
)
""")

conn.commit()


def add_data(date, category, transaction_type, amount):
    cursor.execute(
        "INSERT INTO transactions(date, category, type, amount) VALUES (?, ?, ?, ?)",
        (date, category, transaction_type, amount)
    )
    conn.commit()


def get_data():
    return pd.read_sql_query(
        "SELECT * FROM transactions",
        conn
    )


def update_data(id, date, category, transaction_type, amount):
    cursor.execute(
        """
        UPDATE transactions
        SET date=?, category=?, type=?, amount=?
        WHERE id=?
        """,
        (date, category, transaction_type, amount, id)
    )
    conn.commit()


def delete_data(id):
    cursor.execute(
        "DELETE FROM transactions WHERE id=?",
        (id,)
    )
    conn.commit()