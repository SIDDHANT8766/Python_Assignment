#Accept list from user
#
# filter =  Prime
# map =     Multiply
# reduce =  Find Maximum from it
#


from functools import reduce

def Prime(num):

    for i in range(2,num):
        if(num % i == 0):
            return False
    return True

Mul = lambda No : No * 2

Add = lambda A , B : A if A > B else B

def main():
    print("Enter the length of list :")
    Length = int(input())    

    Data = list()          # Accept list 

    print("Enter the velue of list :")

    for i in range(Length):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(Prime,Data))
    print("Filtered data is :",FData)

    MData = list(map(Mul,FData))
    print("Maped data is :",MData)

    RData = reduce(Add,MData)
    print("Reduced data is :",RData)

if __name__ == "__main__":
    main()