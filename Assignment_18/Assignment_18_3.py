#Accept list from user
#
# filter = No >= 70 and No <= 90
# map = + 10
# reduce = multiply all
#


from functools import reduce

GretLes = lambda No : No >= 70 and No <= 90

Increment = lambda No : No + 10

Product = lambda A , B : A * B

def main():
    print("Enter the length of list :")
    Length = int(input())    # 12

    Data = list()          # Accept list 

    print("Enter the velue of list :")

    for i in range(Length):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(GretLes,Data))
    print("Filtered data is :",FData)

    MData = list(map(Increment,FData))
    print("Maped data is :",MData)

    RData = reduce(Product,MData)
    print("Reduced data is :",RData)

if __name__ == "__main__":
    main()