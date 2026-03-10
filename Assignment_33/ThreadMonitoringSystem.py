import sys
import os
import psutil
import threading


def Display(ProcessName):

    Border = "-"*50
    pboj = psutil.Process()

    fobj = open("Thread_Monitoring.log","w")

    fobj.write(Border+"\n")
    fobj.write("------------ Thread Monitoring System ------------\n")
    fobj.write(Border+"\n")

    fobj.write("Process name is : \n")
    fobj.write(pboj.name()+"\n")

    fobj.write(" \n")

    fobj.write("Process ID is : \n")
    fobj.write(str(os.getpid()))

    fobj.write(" \n")

    fobj.write("Thread count is : \n")
    fobj.write(str(threading.active_count()))

    fobj.write(" \n")

    fobj.write(Border+"\n")

    print("Log file created successfully")



def main():
    
    Display(sys.argv[0])

if __name__ == "__main__":
    main()