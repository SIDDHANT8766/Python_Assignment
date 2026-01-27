def Minimum(List):
    iMin = List[1]

    for i in range(len(List)):
        if(List[i] < iMin):
            iMin = List[i]

    return iMin

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

    Ret = Minimum(Data)
    print("Minimum number of list is : ",Ret)

if __name__ == "__main__":
    main()