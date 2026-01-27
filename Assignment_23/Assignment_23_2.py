class Circle:

    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self,Value):
        print("Radius is :",Value)
        self.Radius = Value


    def CalculateArea(self):

        self.Area = Circle.PI * self.Radius **2

        


    def CalculateCircumference(self):

        self.Circumference = 2 * Circle.PI * self.Radius

        

    def Display(self):
        print("Area is : ",self.Area)
        print("Circumference is : ",self.Circumference)


def main():
    Value = 0

    print("Enter the radius :")
    iNo = int(input())

    cobj = Circle()

    ########################

    cobj.Accept(iNo)

    ########################

    cobj.CalculateArea()

    ########################

    cobj.CalculateCircumference()

    ########################

    cobj.Display()





if __name__ == "__main__":
    main()
