def substring_search(str1, str2):
    index = str1.find(str2)
    return index if index != -1 else -1

str1 = "Hello, World!"
str2 = "World"
print(substring_search(str1, str2))