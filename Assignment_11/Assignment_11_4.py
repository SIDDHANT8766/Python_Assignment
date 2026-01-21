
def main():
    num = int(input("Enter a number: "))
    binary = ""

    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2

    print("Binary equivalent is:", binary)


if __name__ == "__main__":
    main()