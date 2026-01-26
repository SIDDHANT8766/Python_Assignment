def Display(No):
    Count = 0
    Digit = 0
    
    while(No != 0):
        Digit = No % 10
        Count = Count + Digit
        No = No // 10
        
    return Count
                   

def main():
    print("Enter your  :")
    Value = int(input())

    iRet = Display(Value)
    print("Total Addition of number is :",iRet)

if __name__ == "__main__":
    main()