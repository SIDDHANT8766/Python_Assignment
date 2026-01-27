import threading

def EvenTable(Value1):
    Count = 0

    print('Even number are ')
    for i in range(Value1):
        Count = Count + 2
        print(Count)


def OddTable(Value2):
    Count = 1

    print('Odd number are ')
    while Value2 != 0:
        print(Count)
        Count = Count + 2
        Value2 = Value2 - 1


def main():
    

    t1 = threading.Thread(target = EvenTable,args = (10,))
    t2 = threading.Thread(target = OddTable,args = (10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()