# ---------------------------------------------------------
# Open Files Monitoring
# ---------------------------------------------------------

import psutil
import os

def DisplayOpenFiles():

    Border = "-" * 50
    pboj = psutil.Process(os.getpid())

    fobj = open("OpenFilesLog.log", "w")

    fobj.write(Border + "\n")
    fobj.write("----------- Open Files Monitoring -----------\n")
    fobj.write(Border + "\n")

    try:
        files = pboj.open_files()

        fobj.write("Process Name : \n")
        fobj.write(pboj.name() + "\n")

        fobj.write("PID : \n")
        fobj.write(str(pboj.pid) + "\n")

        fobj.write("Number of Open Files : \n")
        fobj.write(str(len(files)) + "\n")

    except:
        fobj.write("Access Denied\n")

    fobj.write("\n" + Border)
    fobj.close()

    print("Open Files Log Created Successfully")


def main():
    DisplayOpenFiles()


if __name__ == "__main__":
    main()