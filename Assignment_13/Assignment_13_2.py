def CountDigits(Value):
    Count = 0

    while(Value != 0):
        Value = Value // 10
        Count = Count + 1
        

    return Count        

def main():
    Ret = None

    print("Enter the number :")
    No = int(input())

    Ret = CountDigits(No)

    print("Total digits in number are :",Ret)


if __name__ == "__main__":

    main()