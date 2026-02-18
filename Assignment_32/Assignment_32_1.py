import sys
import hashlib
import os

def CheckSum(file):

    fobj = open(file,"rb")

    hobj = hashlib.md5()
    
    Buffer = fobj.read(1024)
    
    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()
    

def CalculateCkechSum(Directory):
    
    for FolderName , SubFolderName , FileName in os.walk(Directory):
        for file in FileName:
            FilePath = os.path.join(FolderName, file)
            Ret = CheckSum(FilePath)
            print("Hash for", file, "is :", Ret)

def main():
    
    CalculateCkechSum(sys.argv[1])

if __name__ == "__main__":
    main()