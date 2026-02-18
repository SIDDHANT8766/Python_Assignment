import os
import sys

def CheckFile(Directory,Extention):

    Ret = os.path.exists(Directory)
    if(Ret == False):
        print("Folder is not exist")
        return 

    Ret = os.path.isdir(Directory)
    if(Ret == False):
        print("It is not a folder/Directory")
        return
    
    print("Files are :")
    
    for FolderName, SubFolderName, FileName in os.walk(Directory):
        for file in FileName:
            if(file.endswith(Extention) == True):
                print(file)
    

def main():

    CheckFile(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()