def isPalindrome(s):
    return s == s[::-1]

str_input = "madam"
if isPalindrome(str_input):
    print("1")
else:
    print("0")