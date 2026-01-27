def Addition(List):
    Sum = 0

    for i in range(len(List)):
        Sum = Sum + List[i]
    return Sum

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

    Ret = Addition(Data)
    print("Addition of list is : ",Ret)

if __name__ == "__main__":
    main()