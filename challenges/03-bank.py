print("Welcome to Chase bank.")
print("Have a nice day!")

def deposit(self): 
    amount=float(input("Enter amount to be Deposited: ")) 
    self.balance += amount 
    print("\n Amount Deposited:",amount) 

def withdraw(self): 
    amount = float(input("Enter amount to be Withdrawn: ")) 
    if self.balance>=amount: 
        self.balance-=amount 
        print("\n You Withdrew:", amount) 
    else: 
        print("\n Insufficient balance  ") 

def display(self): 
    print("\n Net Available Balance=",self.balance) 

   

deposit() 
withdraw() 
display() 