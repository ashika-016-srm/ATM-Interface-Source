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

if __name__ == "__main__":
    main()
