def CheckPerfect(Number):

    Sum = 0

    for i in range(1,Number):
        if(Number % i == 0):
            Sum = Sum + i

    return Sum

def main():
    No = 0
    Ret = None

    print("Enter the number :")
    No = int(input())

    Ret = CheckPerfect(No)

    print(Ret)

    if(Ret == No):
        print("Number is perfect ")
    else:
        print("Number is not perfect ")

if __name__ == "__main__":
    main()