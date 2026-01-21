value = input("Enter a value: ")

length = 0
for ch in value:
    length += 1

flag = True
i = 0
j = length - 1

while i < j:
    if value[i] != value[j]:
        flag = False
        break
    i += 1
    j -= 1

if flag:
    print("It is a Palindrome")
else:
    print("It is NOT a Palindrome")
