Add = lambda No1,No2 : No1 + No2

def main():
    print("Enter your number :")
    Value1 = int(input())

    print("Enter your number :")
    Value2 = int(input())

    iRet = Add(Value1,Value2)
    print("Aiddition is :",iRet)

if __name__ == "__main__":
    main()