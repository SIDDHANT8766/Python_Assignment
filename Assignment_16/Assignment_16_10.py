def Display(name):
    Count = 0

    for i in range(len(name)):
        Count = Count + 1  

    print(Count)

def main():
    Value = str
    
    print("Enter your name :")
    Value = str(input())

    Display(Value)

if __name__ == "__main__":
    main()