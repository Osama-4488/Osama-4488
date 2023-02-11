while True:
    balance=10000
    print("      ATM      ")
    print("""
    1)          Balance
    2)          Withdraw
    3)          Deposite
    4)          Quit     
    """)
    try:
        option = int(input("Enter Option: "))
    except Exception as e:
        print('Error: ', e)
        print('Enter 1,2,3 or 4 only')
        continue
    if option==1:
        print("Balance $ ", balance)    

    if option==2:
        print("Balance $ ", balance)
        withdraw = float(input("Enter Withdraw amount $ "))
        if withdraw>0:
            forewardbalance=(balance-withdraw)
            print("forward Balance $ ",forewardbalance)
        elif withdraw>balance:
            print("No funs in account")
        else:
            print('None withdraw made')
    if option==3:
        print("Balance $ ",balance)
        Deposit=float(input("Enter deposit amount $ "))
        if Deposit>0:
            forewardbalance=(balance+Deposit)
            print("Forward Balance $ ", forewardbalance)
        else:
            print("None deposite made")
    if option==3:
        exit()

print('I Love Ilham for ever')
