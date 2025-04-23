import sqlite3

def connect_db():
    return sqlite3.connect("bank.db")

def initialize_db():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                account_number TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                pin TEXT NOT NULL,
                balance REAL DEFAULT 0
            )
        ''')
        conn.commit()
