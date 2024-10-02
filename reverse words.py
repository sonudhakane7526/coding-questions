def reverse_words(s):
    words = s.split()
    if words:
        last_word = words.pop()
        reverse_words(" ".join(words))
        print(last_word, end=" ")

if __name__ == "__main__":
    s = "Hello, World!"
    reverse_words(s)
