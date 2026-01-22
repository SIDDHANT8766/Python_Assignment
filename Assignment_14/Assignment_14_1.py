Square = lambda No : No**2

def main():
    print("Enter your number :")
    Value = int(input())

    iRet = Square(Value)
    print("Square is :",iRet)

if __name__ == "__main__":
    main()