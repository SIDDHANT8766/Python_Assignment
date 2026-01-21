def CheckVowels(Value):

    if(((Value == 'a') or (Value == 'e') or (Value == 'o') or (Value == 'i') or (Value == 'u'))    
      and ((Value == 'A') or (Value == 'E') or (Value == 'O') or (Value == 'I') or (Value == 'U'))):
        print("Its Vowels ")
    else:
        print("Its not Vowels ")


def main():
    print("Enter the Charecter :")
    No = input()

    CheckVowels(No)

if __name__ == "__main__":
    main()