from functools import reduce

maxLength = lambda string : ((len(string)) > 5)

def main():
    print("Enter the length of list :")
    Length = int(input())

    Data = list()

    print("Enter the elemets :")

    for i in range(Length):
        Value = str(input())
        Data.append(Value)

    RData = list(filter(maxLength,Data)) 
    print("String having length 5 is :",RData)

if __name__ == "__main__":
    main()