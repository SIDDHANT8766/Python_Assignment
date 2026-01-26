def Display(No):
    iFact = 1

    for i in range(1,No+1):
        iFact = iFact * i

    return iFact             

def main():
    print("Enter your element :")
    Value = int(input())

    iRet = Display(Value)
    print("Factorial is :",iRet)

if __name__ == "__main__":
    main()