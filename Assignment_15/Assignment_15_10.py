
Divisible = lambda No1 : No1 % 2 == 0

def main():
    print("Enter the length of list :")
    Length = int(input())

    Data = list()

    print("Enter the elemets :")

    for i in range(Length):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(Divisible,Data)) 
    print("Total even elements are:",FData)
    print("Count of even elemets are :",len(FData))

if __name__ == "__main__":
    main()