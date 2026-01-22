from functools import reduce

Min = lambda A,B : A if A < B else B

def main():
    print("Enter the length of list :")
    Length = int(input())

    Data = list()

    print("Enter the elemets :")

    for i in range(Length):
        Value = int(input())
        Data.append(Value)

    RData = reduce(Min,Data) 
    print("Minimum number is :",RData)

if __name__ == "__main__":
    main()