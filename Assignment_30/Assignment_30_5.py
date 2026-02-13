def CheckWord(FileName,Word):

    fobj = open(FileName,"r")

    for line in fobj:
        name = line.split()
        if(Word in name):
            return True
    
    return False

def main():
    
    FileName = input("Enter the Source file name :")
    Word = input("Enter the word :")

    Ret = CheckWord(FileName,Word)

    if(Ret == True):
        print("Word is present")

    else:
        print("Word is not present")


if __name__ == "__main__":
    main()