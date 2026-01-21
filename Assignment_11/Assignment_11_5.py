
def main():
    print("Enter your number :")
    No = int(input())

    if(No >= 75):
        print("Distiction")
    elif(No >= 60):
        print("First Class")
    elif(No >= 50):
        print("Second Class")
    else:
        print("fail")

if __name__ == "__main__":
    main()