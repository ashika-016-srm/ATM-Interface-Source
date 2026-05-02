import os

class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit of ${amount} successful. Current balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return f"Withdrawal of ${amount} successful. Current balance: ${self.balance}"

def main():
    atm = ATM()  # Creating an instance of the ATM class

    while True:
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Your current balance is:", atm.check_balance())
        elif choice == 2:
            amount = float(input("Enter amount to deposit: $"))
            print(atm.deposit(amount))
        elif choice == 3:
            amount = float(input("Enter amount to withdraw: $"))
            print(atm.withdraw(amount))
        elif choice == 4:
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def create_readme():
    readme_content = """
# Simple ATM Interface

This is a simple ATM interface implemented in Python. It allows users to check balance, deposit money, and withdraw money.

## Usage

1. Run the `main()` function to start the ATM interface.
2. Follow the on-screen instructions to interact with the ATM.

## Features

- Check balance
- Deposit money
- Withdraw money

## Author

- [Samrocz05](https://github.com/Samrocz05)

Feel free to contribute and improve this project!

    """
    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)

if __name__ == "__main__":
    create_readme()
    main()
