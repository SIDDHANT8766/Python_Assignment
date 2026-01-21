def Factors(Value):

    print("Output :")
    for i in range(Value,0,-1):
        print("\t",i)

def main():
    print("Enter the number :")
    No = int(input())

    Factors(No)

if __name__ == "__main__":
    main()