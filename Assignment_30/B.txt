def NoOfLine(FileName):

    fobj = open(FileName,"rb")

    Data = fobj.readlines()

    print("Number of lines in file are :",len(Data))

def main():
    
    FileName = input("Enter the file name :")

    iRet = NoOfLine(FileName)

if __name__ == "__main__":
    main()