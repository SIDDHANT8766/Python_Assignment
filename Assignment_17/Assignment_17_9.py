def Display(No):
    Count = 0
    
    while(No != 0):
        No = No // 10
        Count = Count + 1
        
    return Count
                   

def main():
    print("Enter your  :")
    Value = int(input())

    iRet = Display(Value)
    print("Count of number is :",iRet)

if __name__ == "__main__":
    main()