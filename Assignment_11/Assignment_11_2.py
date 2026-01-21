def Area(Radius,PI = 3.14):
    Ans = None
    Ans = PI * Radius * Radius  # PI * Radius**2
    return Ans


def main():
    No = 0
    Ret = 0

    print("Enter the radius of circle :")
    No = int(input())

    Ret = Area(No)

    print("Area of Circle is :",Ret)


if __name__ == "__main__":
    main()