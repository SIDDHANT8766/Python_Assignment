def Factors(Value):

    for i in range(1,Value+1):
        if(Value % i == 0):
            print(i)


def main():
    print("Enter the number :")
    No = int(input())

    Factors(No)

if __name__ == "__main__":
    main()