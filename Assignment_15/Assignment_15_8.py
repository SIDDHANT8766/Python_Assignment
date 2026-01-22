
Divisible = lambda No : No % 3 == 0 and No % 5 == 0

def main():
    print("Enter the length of list :")
    Length = int(input())

    Data = list()

    print("Enter the elemets :")

    for i in range(Length):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(Divisible,Data)) 
    print("Number dividible by 3 and 5 is :",FData)

if __name__ == "__main__":
    main()