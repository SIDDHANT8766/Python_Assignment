import os
import sys
import shutil

def CheckFile(Directory,NewDirectory):

    Ret = os.path.exists(Directory)
    if(Ret == False):
        print("Folder is not exist")
        return 

    Ret = os.path.isdir(Directory)
    if(Ret == False):
        print("It is not a folder/Directory")
        return
    
    Ret = os.mkdir(NewDirectory)

    if(Ret == False):
        print("unable to create folder") 

    
    
    for FolderName, SubFolderName, FileName in os.walk(Directory):
        for file in FileName:
            
            src_path = os.path.join(FolderName,file)

            shutil.copy(src_path,NewDirectory)

        print("File copied successfully")
                
            
    

def main():

    CheckFile(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()