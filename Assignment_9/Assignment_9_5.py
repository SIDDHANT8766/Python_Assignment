def Divisible(Value):

    if((Value % 3 == 0) and (Value % 5 ==0)):
        print("It is Divisible by 3 and 5")

def main():
    print("Enter the number :")
    No = int(input())

    Divisible(No)

if __name__ == "__main__":
    main()