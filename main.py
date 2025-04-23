from db import initialize_db, connect_db
from utils import create_account, close_account, modify_account
from banking import check_balance, deposit, withdraw

# handles user login with account number and pin
def login():
    acc = input("Enter account number: ")
    pin = input("Enter PIN: ")

    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM accounts WHERE account_number = ? AND pin = ?", (acc, pin))
        result = cur.fetchone()

    # returns None if login fails
    return result

# main CLI program loop
def main():
    # set up the database when the program first runs
    initialize_db()

    while True:
        # show login and create account options
        print("\n=== Welcome to CLI Banking System ===")
        print("1. Login")
        print("2. Create Account")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            # user login flow
            user = login()
            if user:
                # greet the user after successful login
                print(f"\nHello, {user[1]}!")
                while True:
                    # show main banking menu
                    print("\n--- Banking Menu ---")
                    print("1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Modify Account")
                    print("5. Close Account")
                    print("6. Logout")

                    action = input("Select an action: ")

                    if action == "1":
                        # check and display current balance
                        balance = check_balance(user[0])
                        print(f"Your balance is: ${balance:.2f}")

                    elif action == "2":
                        # prompt user to enter deposit amount
                        amt = float(input("Enter deposit amount: "))
                        deposit(user[0], amt)
                        print("Deposit successful.")

                    elif action == "3":
                        # prompt user to enter withdrawal amount
                        amt = float(input("Enter withdrawal amount: "))
                        if withdraw(user[0], amt):
                            print("Withdrawal successful.")
                        else:
                            print("Insufficient funds.")

                    elif action == "4":
                        # allow user to change name or pin
                        name = input("New name (leave blank to keep current): ")
                        pin = input("New PIN (leave blank to keep current): ")
                        modify_account(user[0], name=name if name else None, pin=pin if pin else None)
                        print("Account updated.")

                    elif action == "5":
                        # confirm and close account
                        confirm = input("Are you sure you want to close your account? (y/n): ")
                        if confirm.lower() == "y":
                            close_account(user[0])
                            print("Account closed.")
                            break

                    elif action == "6":
                        # logout and return to main menu
                        print("Logging out...")
                        break

                    else:
                        # invalid option handler
                        print("Invalid choice.")

            else:
                # show error if login fails
                print("Invalid account number or PIN.")

        elif choice == "2":
            # create a new account
            acc = input("Choose a new account number: ")
            name = input("Enter your name: ")
            pin = input("Set a 4-digit PIN: ")
            try:
                create_account(acc, name, pin)
                print("Account created successfully.")
            except Exception as e:
                # handle any errors during account creation
                print("Error creating account:", e)

        elif choice == "3":
            # exit the program
            print("Goodbye!")
            break

        else:
            # handle invalid menu selection
            print("Invalid selection.")

# run the CLI banking app
if __name__ == "__main__":
    main()
