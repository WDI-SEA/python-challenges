# Class Declaration with Three Methods..per instructions...
class Bank_Transaction:
    # Constructor Intializer for class Bank
    def __init__(self, current_balance = 0):
        self.current_balance = current_balance

    def get_balance(self):
        return self.current_balance
    
    def withdraw(self, amount):
        self.current_balance -= amount
    
    def deposit(self, amount):
        self.current_balance += amount


# Main Program Loop...
def main ():
    continue_status = "Y"
    current_session = Bank_Transaction(0)
    
    while continue_status == "Y":

        print("What would you like to do: \n 1) Check Account Balance \n 2) Withdraw \n 3) Deposit \n Please Enter a Number Choice: \n")
        transaction = int(input("> "))
        print("\n")

        if transaction == 1:
            print(f"Your current balance is: \t ${current_session.get_balance()}")
        elif transaction == 2:
            amount = float(input("How much do you want to Withdraw?\n> "))
            current_session.withdraw(amount)
            print(f"Your current balance is: \t ${current_session.get_balance()}")
        elif transaction == 3:
            amount = float(input("How much do you want to Deposit \n> "))
            current_session.deposit(amount)
            print(f"Your current balance is: \t ${current_session.get_balance()}")

        print("\n")
        continue_status = input("Do you want to Continue with your transaction? Press Y or N. \n > ")
        if continue_status == "Y":
            transaction = None


    
main()

