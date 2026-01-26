def Prime(No):
    iFact = 0

    for i in range(2,No):
        if(No % i != 0):
            return True
        else:
            return False              

def main():
    print("Enter your element :")
    Value = int(input())

    iRet = Prime(Value)

    if(iRet == True):
        print("Number is prime")
    else:
        print("It is not prime")

if __name__ == "__main__":
    main()