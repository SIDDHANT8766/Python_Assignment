def MultiTable(Value):

    for i in range(1,11):
        print(i * Value)


def main():

    print("Enter the number :")
    No = int(input())
    
    MultiTable(No)


if __name__ == "__main__":
    main()