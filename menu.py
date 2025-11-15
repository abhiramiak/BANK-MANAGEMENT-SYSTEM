from account_operations import *

def menu():
    while True:
        print("\n Bank Management System")
        print("1. CREATE ACCOUNT")
        print("2. VIEW ACCOUNT")
        print("3. DEPOSIT MONEY")
        print("4. WITHDRAW MONEY")
        print("5. CHECK OUT BALANCE")
        print("6. EXIT")

        choice=input("enter your choice")
        
        if choice=="1":
            create_account()
        elif choice=="2":
            view_accounts()
        elif choice=="3":
            deposit_money()
        elif choice=="4":
            withdraw_money()
        elif choice=="5":
            check_balance()
        elif choice=="6":
            print("exiting system")
            break
        else:
            print("invalid choice")



