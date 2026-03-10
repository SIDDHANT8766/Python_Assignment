# ---------------------------------------------------------
# Memory Monitoring
# ---------------------------------------------------------

import psutil
import os

def DisplayMemory():

    Border = "-" * 50
    pboj = psutil.Process(os.getpid())

    fobj = open("MemoryLog.log", "w")

    fobj.write(Border + "\n")
    fobj.write("----------- Memory Monitoring -----------\n")
    fobj.write(Border + "\n")

    mem = pboj.memory_info()

    fobj.write("Process Name : \n")
    fobj.write(pboj.name() + "\n")

    fobj.write("PID : \n")
    fobj.write(str(pboj.pid) + "\n")

    fobj.write("RSS (RAM Used) : \n")
    fobj.write(str(mem.rss) + "\n")

    fobj.write("VMS (Virtual Memory) : \n")
    fobj.write(str(mem.vms) + "\n")

    fobj.write("\n" + Border)
    fobj.close()

    print("Memory Log Created Successfully")


def main():
    DisplayMemory()


if __name__ == "__main__":
    main()