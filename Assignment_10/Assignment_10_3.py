def Factors(Value1,Value2):

    print("Addition is :",Value1 + Value2)

    print("Substraction is :",Value1 - Value2)

    print("Multiplication is :",Value1 * Value2)

    print("Division is :",Value1 / Value2)


def main():
    print("Enter the 1st number :")
    No1 = int(input())

    print("Enter the 2nd number :")
    No2 = int(input())

    Factors(No1,No2)

if __name__ == "__main__":
    main()