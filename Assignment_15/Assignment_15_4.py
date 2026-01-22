from functools import reduce

Add = lambda A,B : A + B

def main():
    print("Enter the length of list :")
    Length = int(input())

    Data = list()

    print("Enter the elemets :")

    for i in range(Length):
        Value = int(input())
        Data.append(Value)

    RData = reduce(Add,Data) 
    print(RData)

if __name__ == "__main__":
    main()