import threading

def Front(No1):
    print("for t1 :")
    for i in range(1,No1+1):
        print(i)

def Reverse(No2):
    print("for t2 :")
    for i in range(No2,0,-1):
        print(i)
     

def main():
 

    t1 = threading.Thread(target = Front, args = (50,))  # Dont use direct list in the args as (args = (11,22,33,44,))
    t2 = threading.Thread(target = Reverse, args = (50,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("Exit of main")

if __name__ == "__main__":
    main()