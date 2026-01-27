def Maximum(List):
    iMax = 0

    for i in range(len(List)):
        if(List[i] > iMax):
            iMax = List[i]

    return iMax

def main():
    Length = 0
    Value = 0

    print("Enter length of list :")
    Length = int(input())

    Data = list()

    print("Enter the values :")

    for i in range(Length):
        Value = int(input())
        Data.append(Value)

    Ret = Maximum(Data)
    print("Maximum number of list is : ",Ret)

if __name__ == "__main__":
    main()