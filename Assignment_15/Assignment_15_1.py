Square = lambda No : No**2

def main():
    print("Enter the length of list :")
    Length = int(input())

    Data = list()

    print("Enter the elemets :")

    for i in range(Length):
        Value = int(input())
        Data.append(Value)

    MData = list(map(Square,Data)) 
    print(MData)

if __name__ == "__main__":
    main()