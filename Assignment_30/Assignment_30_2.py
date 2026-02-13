import os

def NoOfLine(FileName):
    Count = 0

    fobj = open(FileName,"r")

    for line in fobj:
        words = line.split()
        Count = Count + len(words)


    print("Number of lines in file are :",Count)

def main():
    
    FileName = input("Enter the file name :")

    iRet = NoOfLine(FileName)

if __name__ == "__main__":
    main()