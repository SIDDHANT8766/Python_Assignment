import threading

def Maximum(List):
    iMax = 0

    for i in range(len(List)):
        if(List[i] > iMax):
            iMax = List[i]

    print("Maximum number is : ",iMax)
    

def Minimum(List):
    iMin = List[1]

    for i in range(len(List)):
        if(List[i] < iMin):
            iMin = List[i]

    print("Minimum number is : ",iMin)
       

def main():
    print("Enter the lenghth of list :")
    Length = int(input())

    Data = list()

    print("Enter your elements :")

    for i in range(Length):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread(target = Maximum, args = (Data,))
    t2 = threading.Thread(target = Minimum , args = (Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()