from db import connect_db

# checks the current balance for the given account
def check_balance(account_number):
    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
        result = cur.fetchone()
        return result[0] if result else 0.0

# adds the specified amount to the account balance
def deposit(account_number, amount):
    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute("UPDATE accounts SET balance = balance + ? WHERE account_number = ?", (amount, account_number))
        conn.commit()

# subtracts the specified amount if there are sufficient funds
def withdraw(account_number, amount):
    balance = check_balance(account_number)

    # only proceed if there's enough money
    if amount <= balance:
        with connect_db() as conn:
            cur = conn.cursor()
            cur.execute("UPDATE accounts SET balance = balance - ? WHERE account_number = ?", (amount, account_number))
            conn.commit()
        return True
    else:
        return False
