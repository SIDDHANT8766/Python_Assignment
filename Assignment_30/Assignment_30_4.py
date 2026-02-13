def CopyFile(FileName,NewFile):

    fobj1 = open(FileName,"r")
    fobj2 = open(NewFile,"w")


    Data = fobj1.read()

    fobj2.write(Data)

def main():
    
    FileName = input("Enter the Source file name :")
    NewFile = input("Enter the Destination file name :")

    CopyFile(FileName,NewFile)

    print("File copied successfully")

if __name__ == "__main__":
    main()