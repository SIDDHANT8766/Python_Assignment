import sys
import os
import time
import hashlib

def CalculateCheckSum(FilePath):

    fobj = open(FilePath, "rb")
    hobj = hashlib.md5()

    Buffer = fobj.read(1024)
    while Buffer:
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()
    return hobj.hexdigest()


def CalculateDuplicate(Directory):

    Duplicate = {}

    for FolderName, SubFolderName, FileName in os.walk(Directory):
        for file in FileName:
            FilePath = os.path.join(FolderName, file)
            CheckSum = CalculateCheckSum(FilePath)

            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(FilePath)
            else:
                Duplicate[CheckSum] = [FilePath]

    return Duplicate


def MakeLog(Directory):

    Mydict = CalculateDuplicate(Directory)

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    LogFile = os.path.join(Directory, "Sid_%s.log" % timestamp)

    fobj = open(LogFile, "w")

    for files in Mydict.values():

        FileCount = len(files)  

        if FileCount > 1:
            fobj.write("Duplicate files:\n")

            for file in files[1:]:
                fobj.write(file + "\n")
                os.remove(file)

            fobj.write("\n")

    fobj.close()
    print("Log created successfully")


def main():
    MakeLog(sys.argv[1])

if __name__ == "__main__":
    main()
