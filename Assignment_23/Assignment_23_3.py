class Arithmatic:
    
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0


    def Accept(self,No1,No2):

        self.Value1 = No1
        self.Value2 = No2

    def Addition(self):

        return self.Value1 + self.Value2
    

    def Substrction(self):

        return self.Value1 - self.Value2
    
    
    def Miltiplication(self):

        return self.Value1 * self.Value2
    
    
    def Division(self):

        return self.Value1 / self.Value2
    


def main():
    iNo1 = 0
    iNo2 = 0
    Ret = None

    print("Enter first number :")
    iNo1 = int(input())

    print("Enter first number :")
    iNo2 = int(input())

    ############################

    aobj = Arithmatic()

    ############################

    aobj.Accept(iNo1,iNo2)

    ############################

    Ret = aobj.Addition()
    print("Addition is :",Ret)

    ############################

    Ret = aobj.Substrction()
    print("Substrction is :",Ret)

    ############################

    Ret = aobj.Miltiplication()
    print("Miltiplication is :",Ret)

    #############################

    Ret = aobj.Division()
    print("Division is :",Ret)

    ############################

if __name__ == "__main__":
    main()
