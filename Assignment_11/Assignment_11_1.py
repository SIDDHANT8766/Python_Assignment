def Area(Length,Width):
    Ans = None
    Ans = Length * Width
    return Ans


def main():
    No1 = 0
    No2 = 0
    Ret = 0

    print("Enter the length of rectangle :")
    No1 = int(input())

    print("Enter the width of rectangle :")
    No2 = int(input())

    Ret = Area(No1,No2)

    print("Area of rectangle is :",Ret)


if __name__ == "__main__":
    main()