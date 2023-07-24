bal=5000
pin=1234
check=int(input("enter the pin:"))
if(pin==check):
    print("1.balance\n2.withdrawal\n3.deposit")
    option=int(input("choose the option:"))
    if(option==1):
        print(f"current balance is {bal}")
    elif(option==2):
        withdrawal=int(input("how much withdrawal:"))
        if(withdrawal>bal):
            print('insufficient balance')
        else:
            bal=bal-withdrawal
            print("withdrawal amount",bal)

    elif(option==3):
        deposit=int(input("how much deposit:"))
        if(deposit==0):
            print('invalid amount')
        else:
            bal=bal+deposit
            print(f"balance is {bal}")
    else:
        print('wrong option')
else:
    print('invalid pin')














