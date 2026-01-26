def Display(Row,Col):
    for i in range(1,Row+1):

        for j in range(1,Col+1):
            if(i == j or i > j):
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