str = input("Enter the string: ")
revstr = ""
num = len(str)
j = num-1

for i in range(0, num):
    revstr = revstr + str[j]
    j = j-1
print("The reversed string: ",revstr)

if str == revstr:
    print("String is palindrome")
else:
    print("String is not a palindrome")



