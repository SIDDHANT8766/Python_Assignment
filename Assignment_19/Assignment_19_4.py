import threading

def Small(List1):
    print("TID of Small :",threading.get_ident())
    print("Thread name of Small is :",threading.current_thread().name)
    Sum = 0
    for i in range(len(List1)):
        if(List1[i] >= 'a' and List1[i] <= 'z'):
            Sum = Sum + 1

    print("Addition of Samll character are :",Sum)


def Capital(List2):
    print("TID of Capital :",threading.get_ident())
    print("Thread name of Capital is :",threading.current_thread().name)
    Sum = 0
    for i in range(len(List2)):
        if(List2[i] >= 'A' and List2[i] <= 'Z'):
            Sum = Sum + 1

    print("Addition of Capital character are :",Sum)
    

def Digit(List3):
    print("TID of Digit :",threading.get_ident())
    print("Thread name of Digit is :",threading.current_thread().name)
    Sum = 0
    for i in range(len(List3)):
        if(List3[i] >= '0' and List3[i] <= '9'):
            Sum = Sum + 1

    print("Addition of Digit character are :",Sum)
     

def main():
    print("Thread name of main is :",threading.current_thread().name)

    Data = ['a','A','1','N','9','c','u','R','d','S','5']       # Always make a separate list 

    t1 = threading.Thread(target = Small, args = (Data,))  # Dont use direct list in the args as (args = (11,22,33,44,))
    t2 = threading.Thread(target = Capital, args = (Data,))
    t3 = threading.Thread(target = Digit, args = (Data,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Exit of main")

if __name__ == "__main__":
    main()