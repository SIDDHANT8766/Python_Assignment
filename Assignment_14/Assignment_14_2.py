Cube = lambda No : No**3

def main():
    print("Enter your number :")
    Value = int(input())

    iRet = Cube(Value)
    print("Cube is :",iRet)

if __name__ == "__main__":
    main()