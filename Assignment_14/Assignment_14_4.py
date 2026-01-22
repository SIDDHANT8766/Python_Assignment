Cube = lambda No1,No2 : No1 < No2

def main():
    print("Enter your number :")
    Value1 = int(input())

    print("Enter your number :")
    Value2 = int(input())

    iRet = Cube(Value1,Value2)

    if(iRet == True):
        print("minimum number is :",Value1)
    else:
        print("minimum number is :",Value2)

if __name__ == "__main__":
    main()