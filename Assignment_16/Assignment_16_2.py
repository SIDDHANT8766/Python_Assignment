def CheckEvenOdd(No):
    if(No % 2 == 0):
        print("Number is Even")
    else:
        print("Number is Odd")

def main():
    print("Enter your number :")
    Value = int(input())

    CheckEvenOdd(Value)

if __name__ == "__main__":
    main()