import threading

lobj = threading.Lock()

iCnt = 0

def Update1(No):
    global iCnt

    for i in range(No):
        with lobj:
            iCnt = iCnt + 1

    print("For Update1 number is : ",iCnt)
    

def Update2(No):
    global iCnt

    for i in range(No):
        with lobj:
            iCnt = iCnt + 1

    print("For Update2 number is : ",iCnt)
       

def main():

    t1 = threading.Thread(target = Update1, args = (1000000,))
    t1.start()
    t1.join()

    t2 = threading.Thread(target = Update2, args = (1000000,))
    t2.start()
    t2.join()

if __name__ == "__main__":
    main()