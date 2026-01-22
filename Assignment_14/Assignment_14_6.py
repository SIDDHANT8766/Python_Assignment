Even = lambda No : (No % 2 != 0)

def main():
    print("Enter your number :")
    Value1 = int(input())

    iRet = Even(Value1)

    if(iRet == True):
        print("Even number is :",Value1)
    else:
        print("Odd number is :",Value1)

if __name__ == "__main__":
    main()