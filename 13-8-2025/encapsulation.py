# encapsulation does two things 1. wrap code in single unit and 2. make data private and protected


class BankAccount:
    def __init__(self,name, balance, pin):
        self.AccountHolderName = name
        self.__balance = balance  #private
        self.__pin = pin
    def __str__(self):
        return f"Account Holder Name:{self.AccountHolderName}"
    # getter
    def getBalance(self,pin):
        if pin == self.__pin:
         return self.__balance
        return "Invalid pin or BankAccount"
    # setter
    def depositBalance(self,amount):
        if amount >= 0:
            self.__balance+=amount
            return "Balance has been updated"
        return "Invalid Amount"
    
b1 = BankAccount("Ramesh",50000,1236)
# print(b1)
print(b1.getBalance(1236))
print(b1.depositBalance(23000))
print(b1.getBalance(1236))


# class ClassName:
    # constructor
    #attributes
    
    # methods    

# creating an object 
# o1 = ClassName(parameters)