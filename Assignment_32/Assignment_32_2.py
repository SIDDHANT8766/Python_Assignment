import sys
import os    
import time

def MakeLog(Directory):

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    LogFile = os.path.join(Directory,"Sid%s.Log" %timestamp)

    fobj = open(LogFile,"w")

    
    for FolderName , SubFolderName , FileName in os.walk(Directory):
        for file in FileName:
            fobj.write(file)
                                    

def main():
    
    MakeLog(sys.argv[1])

if __name__ == "__main__":
    main()