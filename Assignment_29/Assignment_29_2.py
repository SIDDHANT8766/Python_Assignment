import os

def ReadFile(FileName):

    fobj = open(FileName,"r")

    Data = fobj.read()

    print("Data from file is :",Data)

    #for line in fobj:
        #print(line,end=" ")

    fobj.close()
        


def main():
    print("Enter your file name :")
    FileName = input()

    ReadFile(FileName)

if __name__ == "__main__":
    main()
