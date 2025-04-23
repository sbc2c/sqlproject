from db import initialize_db
from utils import create_account, close_account, modify_account
from banking import check_balance, deposit, withdraw

def login():
    acc = input("Enter account number: ")
    pin = input("Enter PIN: ")
    from db import connect_db
    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM accounts WHERE account_number = ? AND pin = ?", (acc, pin))
        return cur.fetchone()

def main():
    initialize_db()

    while True:
        print("\n1. Login\n2. Create Account\n3. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            user = login()
            if user:
                print(f"\nWelcome, {user[1]}!")
                while True:
                    print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Modify Account\n5. Close Account\n6. Logout")
                    action = input("Choose action: ")

                    if action == "1":
                        print(f"Balance: ${check_balance(user[0]):.2f}")
                    elif action == "2":
                        amt = float(input("Amount to deposit: "))
                        deposit(user[0], amt)
                    elif action == "3":
                        amt = float(input("Amount to withdraw: "))
                        if withdraw(user[0], amt):
                            print("Withdrawal successful.")
                        else:
                            print("Insufficient funds.")
                    elif action == "4":
                        name = input("New name (leave blank to skip): ")
                        pin = input("New PIN (leave blank to skip): ")
                        modify_account(user[0], name=name if name else None, pin=pin if pin else None)
                    elif action == "5":
                        confirm = input("Are you sure? (y/n): ")
                        if confirm.lower() == "y":
                            close_account(user[0])
                            print("Account closed.")
                            break
                    elif action == "6":
                        break
            else:
                print("Invalid credentials.")

        elif choice == "2":
            acc = input("New account number: ")
            name = input("Name: ")
            pin = input("PIN: ")
            create_account(acc, name, pin)
            print("Account created.")

        elif choice == "3":
            break

if __name__ == "__main__":
    main()
