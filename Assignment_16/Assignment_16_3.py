def Add(No1,No2):
    return No1 + No2
    

def main():
    print("Enter your number :")
    Value = int(input())

    print("Enter your number :")
    Value2 = int(input())

    Ret = Add(Value,Value2)
    
    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()