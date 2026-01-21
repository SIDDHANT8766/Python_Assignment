def CountDigits(Value):

    Number = 0
    Sum = 0

    while(Value != 0):
        Number = Value % 10
        print(Number)
        Value = Value / 10

        
           

def main():
    Ret = 0

    print("Enter the number :")
    No = int(input())

    Ret = CountDigits(No)

    print("Addition of Total digits in number are :",Ret)


if __name__ == "__main__":

    main()