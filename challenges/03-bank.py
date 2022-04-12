action = input("would you like to withdraw, display balance, or deposite? (please type display, deposite, or withdraw) \n")
balance = 30


if action == 'display':
    print(f"you have an available balance of ${balance}" )
    print("HAVE A GOOD DAY")
elif action == 'deposite':
        amount_to_deposite = input("how much would you like to deposite? \n" )
        print(f"you have a total balance of ${int(balance) + int(amount_to_deposite)}" )
        print("HAVE A GOOD DAY")
elif action == 'withdraw':
        amount_to_withdraw = input("how much would you like to withdraw? \n" )
        print(f"you have a total balance of ${int(balance) - int(amount_to_withdraw)}" )
        print("HAVE A GOOD DAY")
else: print("invalid action, please try again")
    
            

    
