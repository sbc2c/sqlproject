import sqlite3

# returns a connection object for interacting with the database
def connect_db():
    return sqlite3.connect("bank.db")

# creates the accounts table if it doesn't exist
def initialize_db():
    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            account_number TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            pin TEXT NOT NULL,
            balance REAL DEFAULT 0.0
        )
        """)
        conn.commit()
