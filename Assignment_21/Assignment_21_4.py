# Function return's values to thread 

import threading

lobj = threading.Lock()

def Summetion(List,Result):
    iSum = 0

    for i in range(len(List)):
        with lobj:
            iSum = iSum + List[i]

    Result.append(iSum)
    

def Product(List,Result):
    iProd = 1

    for i in range(len(List)):
        with lobj:
            iProd = iProd * List[i]

    Result.append(iProd)
       

def main():
    Length = 0
    Addition = []
    Multiplication = []

    print("Enter the lenghth of list :")
    Length = int(input())

    Data = list()

    print("Enter your elements :")

    for i in range(Length):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread(target = Summetion, args = (Data,Addition,))
    t1.start()
    t1.join()

    print("Summetion of all element from list is :",Addition)

    t2 = threading.Thread(target = Product, args = (Data,Multiplication,))
    t2.start()
    t2.join()

    print("Multiplication of all element from list is :",Multiplication)

if __name__ == "__main__":
    main()