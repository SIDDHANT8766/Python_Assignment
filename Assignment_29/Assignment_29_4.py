import sys
import hashlib

def ComparesFiles(File1 , File2):

    fobj1 = open(File1,"rb")
    fobj2 = open(File2,"rb")

    #######################################

    hobj1 = hashlib.md5()

    Buffer1 = fobj1.read(1024)

    while(len(Buffer1) > 0):
        hobj1.update(Buffer1)
        Buffer1 = fobj1.read(1024)

    fobj1.close()

    ############################################

    hobj2 = hashlib.md5()

    Buffer2 = fobj2.read(1024)

    while(len(Buffer2) > 0):
        hobj2.update(Buffer2)
        Buffer2 = fobj2.read(1024)

    fobj2.close()


    return hobj1.hexdigest(),hobj2.hexdigest()
    
        
def main():
  
    iRet1,iRet2 = ComparesFiles(sys.argv[1], sys.argv[2])

    if(iRet1 == iRet2):
        print("Files are same")
    else:
        print("Files are not same")

if __name__ == "__main__":
    main()
