def Display(No):
    Even = 0

    while(No != 0):
        Even = Even + 2   
        print(Even,end="  ")
        No -= 1   

def main():
    print("Enter your number :")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()