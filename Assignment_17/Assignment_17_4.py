def AddFact(No):
    iFact = 0

    for i in range(1,No):
        if(No % i == 0):
            iFact = iFact + i

    return iFact             

def main():
    print("Enter your element :")
    Value = int(input())

    iRet = AddFact(Value)
    print("Add of Factorial is :",iRet)

if __name__ == "__main__":
    main()