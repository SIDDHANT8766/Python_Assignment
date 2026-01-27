import threading

def EvenListAdd(List1):
    Sum = 0
    for i in range(len(List1)):
        if(List1[i] % 2 == 0):
                Sum = Sum + List1[i]

    print("Addition of Even element is :",Sum)

def OddListAdd(List2):
    Sum = 0
    for i in range(len(List2)):
        if(List2[i] % 2 != 0):
                Sum = Sum + List2[i]

    print("Addition of Odd element is :",Sum)

def main():

    Data = [20,33,34,66,79,11,21,55,2]       # Always make a separate list 

    t1 = threading.Thread(target = EvenListAdd, args = (Data,))  # Dont use direct list in the args as (args = (11,22,33,44,))
    t2 = threading.Thread(target = OddListAdd, args = (Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit of main")

if __name__ == "__main__":
    main()