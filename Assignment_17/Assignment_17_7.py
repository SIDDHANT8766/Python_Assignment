def Display(Row,Col):
    for i in range(Row):

        for j in range(1,Col+1):
            print(j,end="   ") 
        print()
                   

def main():
    print("Enter your row :")
    Value = int(input())

    print("Enter your column :")
    Value2 = int(input())

    Display(Value,Value2)

if __name__ == "__main__":
    main()