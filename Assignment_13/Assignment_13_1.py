def CheckPrime(Value):
    bFlag = False

    for i in range(2,Value):
        if((Value % i) == 0):
            bFlag = True

    return bFlag        

def main():
    Ret = None

    print("Enter the number :")
    No = int(input())

    Ret = CheckPrime(No)

    if(Ret == True):
        print("It is niot prime number")
    else:
        print("Its s prime number")

if __name__ == "__main__":
    main()