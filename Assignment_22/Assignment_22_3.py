# Imp :-  Numbers 
#             Prime,Perfect,Factors,SumFactors

class Numbers:

    def __init__(self,A):
        self.Value = A


    def ChkPrime(self):

        for i in range(2,self.Value):
            if(self.Value % i == 0):
                return False
        
        return True
    
    def Factors(self):

        print("Factors are :")

        for i in range(1,self.Value):
            if(self.Value % i == 0):
                print(i,end="  ")
        print()

    def Perfect(self):
        Sum = 0

        for i in range(1,self.Value):
            if(self.Value % i == 0):
                Sum = Sum + i

        if(Sum == self.Value):
            return True
        else:
            return False
        
        
    def SumFactors(self):
        iSum = 0

        for i in range(1,self.Value):
            if(self.Value % i == 0):
                iSum = iSum + i

        return iSum

def main():
    Number = 0
    Ret = None

    print("Enter your number :")
    Number = int(input())

    nobj = Numbers(Number)

    #######################################

    Ret = nobj.ChkPrime()

    if(Ret == True):
        print("Number is Prime")
    else:
        print("Its not prime")

    #####################################

    nobj.Factors()

    #######################################

    Ret = nobj.Perfect()

    if(Ret == True):
        print("Number is perfect")
    else:
        print("It is not perfect")

    #######################################

    Ret = nobj.SumFactors()
    print("Sum of all factor of number is :",Ret)

    #######################################
    
if __name__ == "__main__":
    main()