from Assignment_17_1Header import Add,Sub,Mul,Div

def main():
    print("Enter your 1 number :")
    Value1 = int(input())

    print("Enter your 2 number :")
    Value2 = int(input())

    iRet = Add(Value1,Value2)
    print("Addition is :",iRet)

    iRet = Sub(Value1,Value2)
    print("Substraction is :",iRet) 

    iRet = Mul(Value1,Value2)
    print("Multiplication is :",iRet)

    iRet = Div(Value1,Value2)
    print("Division is :",iRet)

if __name__ == "__main__":
    main()