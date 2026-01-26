def Display(No):

    for i in range(No):
        print("*",end=" ")      

def main():
    print("Enter your number :")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()