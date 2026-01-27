import threading

def EvenFactorAdd(Value1):
    Sum = 0
    for i in range(2,Value1):
        if(Value1 % i == 0):
            if(i % 2 == 0):
                Sum = Sum + i

    print("Addition of Even factorial is :",Sum)


def OddFactorAdd(Value1):
    Sum = 0
    for i in range(2,Value1):
        if(Value1 % i == 0):
            if(i % 2 != 0):
                Sum = Sum + i

    print("Addition of Odd factorial is :",Sum)

def main():
    

    t1 = threading.Thread(target = EvenFactorAdd,args = (20,))
    t2 = threading.Thread(target = OddFactorAdd,args = (20,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit of main")

if __name__ == "__main__":
    main()