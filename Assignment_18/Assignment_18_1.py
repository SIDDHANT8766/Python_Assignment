PowerofTo = lambda No: No**2 

def main():
    Value = 0
    Ret = 0
    print("Enter your number :")
    Value = int(input())

    Ret = PowerofTo(Value)

    print("Power of 2 of that number is :",Ret)

if __name__ == "__main__":
    main()