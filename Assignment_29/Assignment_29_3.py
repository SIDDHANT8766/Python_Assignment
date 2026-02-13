import sys

def ReadWriteFile(FileName,SourceFile):

    fobj1 = open(SourceFile,"r")

    fobj2 = open(FileName,"w")

    Data = fobj1.read()

    fobj2.write(Data)


    fobj1.close()
    fobj2.close()
        


def main():
    print("Enter your file name in which you want to copy :")
    FileName = input()

    ReadWriteFile(FileName, sys.argv[1])

if __name__ == "__main__":
    main()
