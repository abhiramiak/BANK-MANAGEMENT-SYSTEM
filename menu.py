from account_operations import *

def menu():
    bank = BankOperations() 
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
            bank.create_account()
        elif choice=="2":
            bank.view_accounts()
        elif choice=="3":
            bank.deposit_money()
        elif choice=="4":
            bank.withdraw_money()
        elif choice=="5":
            bank.check_balance()
        elif choice=="6":
            print("exiting system")
            break
        else:
            print("invalid choice")




