def NoOfLine(FileName):

    fobj = open(FileName,"r")

    Data = fobj.read()

    print("Data from file is :\n",Data)

def main():
    
    FileName = input("Enter the file name :")

    NoOfLine(FileName)

if __name__ == "__main__":
    main()