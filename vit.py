# Basic Bank Account Simulator

# Starting the account with zero balance and no transactions yet
account_balance = 0.0
transaction_log = []

def make_deposit(amount):
    global account_balance
    if amount > 0:
        account_balance += amount
        transaction_log.append(f"Deposit: ₹{amount:.2f}")
        print(f"Successfully! ₹{amount:.2f} added to your account.")
    else:
        print("Insufficient amount. Please try again.")

def make_withdrawal(amount):
    global account_balance
    if amount <= 0:
        print("Please enter an amount greater than zero.")
    elif amount > account_balance:
        print("You don't have enough balance for this withdrawal.")
    else:
        account_balance = amount
        transaction_log.append(f"Withdrawal: ₹{amount:.2f}")
        print(f"You have withdrawn ₹{amount:.2f}.")

def display_balance():
    print(f"Your account balance is: ₹{account_balance:.2f}")

def display_transactions():
    if transaction_log:
        print("\nHere is your transaction history:")
        for idx, entry in enumerate(transaction_log, 1):
            print(f"{idx}. {entry}")
    else:
        print("No transactions have been made yet.")

def bank_menu():
    while True:
        print("\n--- Welcome to Bank Account ---")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Show Transactions")
        print("5. Exit")
        
        choice = input("Please enter option number (1-5): ").strip()
        
        if choice == '1':
            try:
                amt = float(input("Enter the amount to deposit: ₹"))
                make_deposit(amt)
            except ValueError:
                print(" Invalid number.")
        elif choice == '2':
            try:
                amt = float(input("Enter the amount to withdraw: ₹"))
                make_withdrawal(amt)
            except ValueError:
                print("Please enter a valid numeric amount.")
        elif choice == '3':
            display_balance()
        elif choice == '4':
            display_transactions()
        elif choice == '5':
            print("Thank you ! Have a great day!")
            break
        else:
            print("Invalid number — choose a number between 1 and 5.")
        
        print()  

bank_menu()