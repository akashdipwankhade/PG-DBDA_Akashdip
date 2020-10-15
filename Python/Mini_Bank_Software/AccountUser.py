from AccountModule import *
import sys
print()
print("-*"*15)
print()
print("\tBanking System")
print()
print("-*"*15)

while True:
    print("-*"*15)
    print("\t MENU")
    print("1. Create New Account")
    print("2. Deposit into Account")
    print("3. Withdraw from Account")
    print("4. Check Balance")
    print("5. Close Account")
    print("6. Exit")
    ch=int(input("Enter Your Choice: "))

    if ch==6:
        exiting()
        sys.exit()
    
    elif ch==1:       
        print("1. Savings\n2. Current")
        acctyp=int(input("Select Account Type: "))
        if create_Account(acctyp):
            print("Account Added Successfully...")
        else:
            print("Entered Wrong Account Type...")

    elif ch==2:
        acc_id=input("Enter Accoount Id: ")
        amt=int(input("Enter Amount to Add: "))
        flag=deposit(acc_id,amt)
        if flag:
            print("Amount Added SuccessFully...")
        else:
            print("Account Not Found..")

    elif ch==3:
        flag=False
        acc_id=input("Enter Accoount Id: ")
        amt=int(input("Enter Amount to Withdraw: "))
        flag=withdrawAmt(acc_id,amt)
        if flag:
            print("Transaction SuccessFully...")
        else:
            print("Transaction Failed...")

    elif ch==4:
        acc_id=input("Enter Accoount Id: ")
        flag=getBalance(acc_id)
        if flag!=True:
             print("Account Not Found..")
           

    elif ch==5:
        acc_id=input("Enter Accoount Id: ")
        flag=deleteAccount(acc_id)
        if flag:
            print("Account Deleted SuccessFully...")
        else:
            print("Account Not Found..")

    else:
        print("You Have Entered Wrong Option...")

    print("-*"*20)