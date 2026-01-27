import threading

def CheckPrime(No):
    
    for i in range(2,No):
        if(No % i == 0):
            return False
            
    return True

def Prime(List):

    PrimeList = []
    NonPrimeList = []

    for i in range(len(List)):
        if(CheckPrime(List[i])):
            PrimeList.append(List[i])
        else:
            NonPrimeList.append(List[i])

    print("Elements which are prime is :",PrimeList)
   


def NonPrime(List): 

    PrimeList = []
    NonPrimeList = []

    for i in range(len(List)):
        if(CheckPrime(List[i])):
            PrimeList.append(List[i])
        else:
            NonPrimeList.append(List[i])

    print("Elements which are nonprime is :",NonPrimeList)
            

def main():
    print("Enter the lenghth of list :")
    Length = int(input())

    Data = list()

    print("Enter your elements :")

    for i in range(Length):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread(target = Prime, args = (Data,))
    t2 = threading.Thread(target = NonPrime , args = (Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()