print("Welcome to Chase bank.")
print("Have a nice day!")

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
            return self.balance
        else:
            self.balance -= amount
            return self.balance

    def check_balance(self):
        return self.balance


def main():
    account = BankAccount()
    
    while True:
        print(f"Your current balance is\n{account.check_balance()}")
        action = input("What would you like to do? (deposit, withdraw, check_balance)\n")
        
        if action.lower() == "deposit":
            amount = float(input("How much would you like to deposit?\n"))
            account.deposit(amount)
        elif action.lower() == "withdraw":
            amount = float(input("How much would you like to withdraw?\n"))
            account.withdraw(amount)
        elif action.lower() == "check_balance":
            pass
        else:
            print("Invalid action. Please enter 'deposit', 'withdraw' or 'check_balance'.")

        done = input("Are you done? (yes/no)\n")
        if done.lower() == 'yes':
            print("Thank you!")
            break


if __name__ == "__main__":
    main()
