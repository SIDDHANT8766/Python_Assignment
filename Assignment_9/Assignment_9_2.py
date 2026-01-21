def CheckGreater(Value1,Value2):

    if(Value1 > Value2):
        print("Value greter is :",Value1)
    else:
        print("Value greater is :",Value2)

    

def main():
    print("Enter the first number :")
    No1 = int(input())

    print("Enter the second number :")
    No2 = int(input())

    CheckGreater(No1,No2)

if __name__ == "__main__":
    main()