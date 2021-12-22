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

        print("What would you like to do: \n 1) check_balance \n 2) deposit \n 3) widthdraw \n")
        transaction = int(input("> "))

        if transaction == 1:
            print(current_session.get_balance())
        elif transaction == 2:
            amount = float(input("How much do you want to Withdraw?\n >"))
            current_session.withdraw(amount)
            print(current_session.get_balance())
        elif transaction == 3:
            amount = float(input("How much do you want to Deposit \n >"))
            current_session.deposit(amount)
            print(current_session.get_balance())

        continue_status = input("Do you want to Log Out? Press Y or N. \n > ")

    
main()

