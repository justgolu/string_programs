def palindrome(str):
    
    for i in range(0, int(len(str))):
        if(str[i] != str[len(str)-i-1]):
            return False
        else:
            return True

res = input("Enter the string: ")
s = palindrome(res)
if(s):
    print("The String is palindrome")
else:
    print("The String is not palindrome")


