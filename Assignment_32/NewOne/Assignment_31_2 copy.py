import os
import sys

def CheckFile(Directory,Extention1,Extention2):

    Ret = os.path.exists(Directory)
    if(Ret == False):
        print("Folder is not exist")
        return 

    Ret = os.path.isdir(Directory)
    if(Ret == False):
        print("It is not a folder/Directory")
        return
    
    
    for FolderName, SubFolderName, FileName in os.walk(Directory):
        for file in FileName:
            if(file.endswith(Extention1) == True):

                old_path = os.path.join(FolderName,file)

                new_file = file.replace(Extention1,Extention2)

                new_path = os.path.join(FolderName,new_file)

                os.rename(old_path,new_path)
                
            
    

def main():

    CheckFile(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__ == "__main__":
    main()