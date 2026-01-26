#Accept list from user
#
# filter =  even
# map =     square
# reduce =  Add
#


from functools import reduce

Even = lambda No : No % 2 == 0

Square = lambda No : No ** 2

Add = lambda A , B : A + B

def main():
    print("Enter the length of list :")
    Length = int(input())    

    Data = list()          # Accept list 

    print("Enter the velue of list :")

    for i in range(Length):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(Even,Data))
    print("Filtered data is :",FData)

    MData = list(map(Square,FData))
    print("Maped data is :",MData)

    RData = reduce(Add,MData)
    print("Reduced data is :",RData)

if __name__ == "__main__":
    main()