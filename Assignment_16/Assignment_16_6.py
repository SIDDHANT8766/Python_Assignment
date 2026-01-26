def Display(No):
    if(No == 0):
        print("Zero")
    elif(No < 0):
        print("Number is negative")
    else:
        print("Number is positive")
        

def main():
    print("Enter your number :")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()