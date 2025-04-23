from db import connect_db

# creates a new account with given account number, name, and pin
def create_account(account_number, name, pin):
    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO accounts (account_number, name, pin, balance) VALUES (?, ?, ?, ?)", (account_number, name, pin, 0.0))
        conn.commit()

# deletes an account based on the account number
def close_account(account_number):
    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM accounts WHERE account_number = ?", (account_number,))
        conn.commit()

# updates the account holder's name or pin
def modify_account(account_number, name=None, pin=None):
    with connect_db() as conn:
        cur = conn.cursor()

        # update name if provided
        if name:
            cur.execute("UPDATE accounts SET name = ? WHERE account_number = ?", (name, account_number))

        # update pin if provided
        if pin:
            cur.execute("UPDATE accounts SET pin = ? WHERE account_number = ?", (pin, account_number))

        conn.commit()
