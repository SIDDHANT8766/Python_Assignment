def Compare(FileName, Str):
    Count = 0
    fobj = open(FileName, "r")

    Data = fobj.read(1024)
    while Data:
        Count = Count + Data.count(Str)
        Data = fobj.read(1024)

    fobj.close()
    return Count

def main():
    FileName = input("Enter the name of file : ")
    StringName = "if"

    iRet = Compare(FileName, StringName)
    print("Total counts of comparison is :", iRet)

if __name__ == "__main__":
    main()
