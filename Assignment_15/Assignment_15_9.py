from functools import reduce

Divisible = lambda No1,No2 : No1 * No2

def main():
    print("Enter the length of list :")
    Length = int(input())

    Data = list()

    print("Enter the elemets :")

    for i in range(Length):
        Value = int(input())
        Data.append(Value)

    FData = reduce(Divisible,Data) 
    print("Multiplication is :",FData)

if __name__ == "__main__":
    main()