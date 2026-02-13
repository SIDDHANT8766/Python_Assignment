import os

def CheckFile(FileName):

    for FolderName , SubFolderName, Files in os.walk(os.path.curdir):

        for file in Files:
            if(file == FileName):
                return True
            
        return False

def main():
    print("Enter your file name :")
    FileName = input()

    bRet = CheckFile(FileName)

    if(bRet == True):
        print("File is present")
    else:
        print("Its not present")

if __name__ == "__main__":
    main()
