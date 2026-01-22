Max = lambda No1,No2,No3: No1  if(No1 > No2 and No1 > No3) else(No2 if No2 > No3 and No2 > No1 else No3)

def main():
    print("Enter your number :")
    Value1 = int(input())

    print("Enter your number :")
    Value2 = int(input())

    print("Enter your number :")
    Value3 = int(input())

    iRet = Max(Value1,Value2,Value3)
    print("maximum is :",iRet)

if __name__ == "__main__":
    main()