def Factorial(Value):

    for i in range(1,Value+1):
        if(i % 2 == 0):
            print(i)   

def main():

    print("Enter the number :")
    No = int(input())
    
    Factorial(No)
    
if __name__ == "__main__":
    main()