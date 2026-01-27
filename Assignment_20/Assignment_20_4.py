def Frequency(List,iFind):
    Count = 0

    for i in range(len(List)):
        if(List[i] == iFind):
            Count = Count + 1

    return Count

def main():
    Length = 0
    Value = 0
    iNo = 0

    print("Enter length of list :")
    Length = int(input())

    Data = list()

    print("Enter the values :")

    for i in range(Length):
        Value = int(input())
        Data.append(Value)
    
    print("Which number you want to search : ")
    iNo = int(input())

    Ret = Frequency(Data,iNo)
    print("Frequency number of list is : ",Ret)

if __name__ == "__main__":
    main()