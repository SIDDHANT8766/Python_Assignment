Even = lambda No : No % 2 == 0

def main():
    print("Enter the length of list :")
    Length = int(input())

    Data = list()

    print("Enter the elemets :")

    for i in range(Length):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(Even,Data)) 
    print(FData)

if __name__ == "__main__":
    main()