from Assignment_20_5Module import ChkPrime

def ListPrime(List):
    Sum = 0

    for i in range(len(List)):
        if(ChkPrime(List[i])):
            Sum = Sum + List[i]
    
    return Sum


def main():
    Length = 0
    Value = 0

    print("Enter length of list :")
    Length = int(input())

    Data = []

    print("Enter the data of list :")

    for i in range(Length):
        Value = int(input())
        Data.append(Value)

    Ret = ListPrime(Data)
    print("Addition of prime number is :",Ret) 

if __name__ == "__main__":
    main()