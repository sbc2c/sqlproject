from db import connect_db

def create_account(account_number, name, pin):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO accounts (account_number, name, pin) VALUES (?, ?, ?)", (account_number, name, pin))
        conn.commit()

def close_account(account_number):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM accounts WHERE account_number = ?", (account_number,))
        conn.commit()

def modify_account(account_number, name=None, pin=None):
    with connect_db() as conn:
        cursor = conn.cursor()
        if name:
            cursor.execute("UPDATE accounts SET name = ? WHERE account_number = ?", (name, account_number))
        if pin:
            cursor.execute("UPDATE accounts SET pin = ? WHERE account_number = ?", (pin, account_number))
        conn.commit()
