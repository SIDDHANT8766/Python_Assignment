from functools import reduce

Max = lambda A,B : A if A > B else B

def main():
    print("Enter the length of list :")
    Length = int(input())

    Data = list()

    print("Enter the elemets :")

    for i in range(Length):
        Value = int(input())
        Data.append(Value)

    RData = reduce(Max,Data) 
    print("Maximum number is :",RData)

if __name__ == "__main__":
    main()