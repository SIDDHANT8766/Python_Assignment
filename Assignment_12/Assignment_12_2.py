def Sum(Value):

    iSum = 0
    for i in range(Value+1):
        iSum = iSum + i

    print("Summetion is :",iSum)

def main():

    print("Enter the number :")
    No = int(input())
    
    Sum(No)


if __name__ == "__main__":
    main()