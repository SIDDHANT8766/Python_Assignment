Even = lambda No : (No % 5 == 0)

def main():
    print("Enter your number :")
    Value1 = int(input())

    iRet = Even(Value1)

    if(iRet == True):
        print("It is divisible by 5")
    else:
        print("It is not divisible by 5")

if __name__ == "__main__":
    main()