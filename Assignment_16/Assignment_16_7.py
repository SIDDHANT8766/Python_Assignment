def Display(No):
    if(No % 5 == 0):
        return True
    else:
        return False      

def main():
    print("Enter your number :")
    Value = int(input())

    iRet = Display(Value)

    print(iRet)

if __name__ == "__main__":
    main()