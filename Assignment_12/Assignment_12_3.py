def Factorial(Value):

    iFact = 1
    for i in range(1,Value+1):
        iFact = iFact * i

    print("Factorial is :",iFact)

def main():

    print("Enter the number :")
    No = int(input())
    
    Factorial(No)
    
if __name__ == "__main__":
    main()