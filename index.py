total_balance = 10000
pin = 1234
pin_code = int(input("Enter you pin !!! "))
if (pin==pin_code):
    print("Welcome")
    
    choose = int(input("choose\nselect 1: for check balance \nselect 2: for withdraw \nselect 3: for fast cash:\n"))
    
    if(choose==1):
        print(total_balance)
    elif choose==2:
        withdraw = int(input("Type your amount:"))
        if withdraw<=total_balance:
            total_balance-= withdraw
            print("Now Your Balance Is = ",total_balance)
        else:
            print("Insufficient balance")
    elif choose==3:
        
        fast_cash= int(input("Choose:\n1: for 2000\n2: for 4000\n3: for 6000\n4: for 10000 "))
        if fast_cash in [1,2,3,4]:
            cash_amount={1: 2000, 2: 4000, 3: 6000, 4: 10000}[fast_cash]
            if cash_amount<=total_balance:
                total_balance-=cash_amount
                print("Now Your Balace Is ",total_balance)
            else:
                print("Insufficient balance")
                
        else:
             print("Invalid choice")       
            
    else:
        print("Invalid number ")
else:
    print("Invalid pin")
print("Thank you for your visit!")
