from abc import ABC,abstractclassmethod

class ACCOUNT(ABC):
    def __init__(self, Aid="",name="",balance=0):
        self._Aid=Aid
        self._name=name
        self._balance=balance
    
    def __str__(self):
        return "Id: "+self._Aid+"\nName: "+self._name+"\nBalance: "+str(self._balance)
    
    def get_balance(self):
        return self._balance
    def get_id(self):
        return self._Aid
    def get_name(self):
        return self._name
    
    def set_balance(self,bal):
        self._balance=bal
    def set_id(self,ad):
        self._Aid=ad
    def set_name(self,nme):
        self._name=nme

    def deposit(self,amt=0):
        self.set_balance(self._balance+amt)
        return True

    def check_balance(self):
        print("Balance of Account Id: ",self._Aid," is : ",self._balance)
        return True
    
    @abstractclassmethod
    def withdraw(self,amt):
        pass

    @abstractclassmethod
    def getDisplay(self):
        pass

class SAVINGS(ACCOUNT):
    sinterestrate=0.04
    sminbal=5000
    def __init__(self,Aid="",name="",balance=0,chequeNo=0):
        super().__init__(Aid,name,balance)
        self.__chequeNo=chequeNo
    
    def __str__(self):
        return super().__str__()+"\nCheque Book Number: "+self.__chequeNo

    def getChequeNo(self):
        return self.__chequeNo
    def setChequeNo(self, cq):
        self.__chequeNo=cq
    
    def withdraw(self,amt):
        if (SAVINGS.sminbal+amt<=self._balance):
            self.set_balance(self._balance-amt)
            return True
        else:
            print("Insufficient Funds..")
            return False
    
    def getInterest(self):
        return self._balance*SAVINGS.sinterestrate
    
    def getDisplay(self):
        return self.__str__()
    
class CURRENT(ACCOUNT):
    cintrestrate=0.02
    cminibal=0
    def __init__(self,Aid="",name="",balance=0,notry=0):
        super().__init__(Aid,name,balance)
        self.__notry=notry
    
    def __str__(self):
        return super().__str__()+"\nNumber Of Transactions: "+self.__notry

    def getNotryNo(self):
        return self.__notry
    def setNotryNo(self, nq):
        self.__notry=nq
    
    def withdraw(self,amt):
        if(CURRENT.cminibal+amt<=self._balance):
            self.set_balance(self._balance-amt)
            return True    
        else:
            print("Insufficient Funds..")
            return False

    def getInterest(self):
        return self._balance*CURRENT.cintrestrate
    
    def getDisplay(self):
        return self.__str__()


