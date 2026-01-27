# Imp :-  Bankaccount 
#             Display,Deposite,Withdrwal,CalculateInterest


class BankAccount:
    ROI = 10.5

    def __init__(self,A,B):
        self.Name = A
        self.Amount = B
        

    def Dispaly(self):
        print(f"Account Holde is : {self.Name} and Current balance is {self.Amount}")


    def Deposit(self,nMoney):

        self.Amount = self.Amount + nMoney

        print("New ammount is :",self.Amount)


    def Withdraw(self,wMoney):
        
        self.Amount = self.Amount - wMoney

        print("Amount after withrawal is :",self.Amount)


    def CalculateInterest(self):
        Interest = None

        Interest = (self.Amount  * BankAccount.ROI) / 100

        return Interest
    

def main():
    Value1 = 0
    Value2 = 0

    bobj = BankAccount("Siddhant",10000)
    bobj.Dispaly()

    print("-"*40)

    #############################################

    print("Enter amount you want to add : ")
    Value1 = int(input())

    bobj.Deposit(Value1)
    bobj.Dispaly()

    print("-"*40)

    ################################################

    print("Enter money you want to withraw : ")
    Value2 = int(input())

    bobj.Withdraw(Value2)
    bobj.Dispaly()

    print("-"*40)

    ################################################

    Ret = bobj.CalculateInterest()
    print("Current interest is :",Ret)

if __name__ == "__main__":
    main()