from AccountClass import *


def readData():
    lst1=[]
    with open("BankAccounts.txt","r") as ra:
        lst_FILE=ra.readlines()
        #print(lst)
        for l in lst_FILE:
            #print(l)
            l=l.rstrip("\n")
            #print(l)
            li=l.split("|")
            if li[3]=="Savings":
                ac=SAVINGS(Aid=li[0],name=li[1],balance=li[2],chequeNo=li[4])
                
            if li[3]=="Current":
                ac=CURRENT(Aid=li[0],name=li[1],balance=li[2],notry=li[4])
            
            lst1.append(ac)
    return lst1    


acc_lst=readData()

def create_Account(acctyp):
    if acctyp <3:
        aid=input("Enter Account Id: ")
        nme=input("Enter Name of Account Holder: ")
        bal=int(input("Enter Balance: "))
        if acctyp==1:
            chn=input("Enter Cheque Number: ")
            ac=SAVINGS(Aid=aid,name=nme,balance=bal,chequeNo=chn)
            acc_lst.append(ac)
            #print(acc_lst)
            return True
            
        if acctyp==2:
            ntry=input("Enter Number of Transaction: ")
            ac=CURRENT(Aid=aid,name=nme,balance=bal,notry=ntry)
            acc_lst.append(ac)
            #print(acc_lst)
            return True  
    else:
        return False
    
    
def searchAccount(acc_id):
    for ob in acc_lst:
        if ob.get_id()==acc_id:
            #print(ob)
            return ob
    return None

def deposit(acc_id,amt):
    ob=searchAccount(acc_id)
    if ob!=None:
        ob.deposit(amt)
        return True
    else:
        return False

def withdrawAmt(acc_id,amt):
    ob=searchAccount(acc_id)
    if ob!=None:
        flag=ob.withdraw(amt)
        #print(flag)
        return flag
    else:
        return False

def getBalance(acc_id):
    ob=searchAccount(acc_id)
    if ob!=None:
        return ob.check_balance()
    else:
        print("Account Not Found...")
        return False

def deleteAccount(acc_id):
    for i,ob in enumerate(acc_lst):
        if ob.get_id()==acc_id:
            acc_lst.pop(i)
            return True
    return False

def getType(ob):
    if isinstance(ob, CURRENT):
        return "Current"
    if isinstance(ob, SAVINGS):
        return "Savings"

def writeData(acc_lst):
    with open("BankAccounts.txt",'w') as aba:
        for ob in acc_lst:
            st=""
            aid=ob.get_id()
            name=ob.get_name()
            bal=ob.get_balance()
            type=getType(ob)
            extr=0
            if type=="Savings":
                extr=ob.getChequeNo()
            else:
                extr=ob.getNotryNo()
            st=str(aid)+"|"+name+"|"+str(bal)+"|"+type+"|"+str(extr)+"\n"
            aba.write(st)
        
def exiting():
    writeData(acc_lst)
    print("Data Successfully Saved into 'BankAccounts.txt' File..")
