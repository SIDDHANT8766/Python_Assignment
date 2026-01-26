def Display(Row,Col):

    for i in range(Row):
        
        for j in range(Col,0,-1):
                if(i < j):
                    print("*",end="  ")
                else:
                    print(" ",end="  ")
        print()
                      

def main():
    print("Enter your Row :")
    Value1 = int(input())

    print("Enter your Column :")
    Value2 = int(input())

    Display(Value1,Value2)

if __name__ == "__main__":
    main()