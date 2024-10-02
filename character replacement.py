def replace_characters(s, ch1, ch2):
    modified_str = []
    for c in s:
        if c == ch1:
            modified_str.append(ch2)
        elif c == ch2:
            modified_str.append(ch1)
        else:
            modified_str.append(c)
    return ''.join(modified_str)

if __name__ == "__main__":
    s = "apples"
    ch1 = 'a'
    ch2 = 'p'
    modified_string = replace_characters(s, ch1, ch2)
    print("Modified string:", modified_string)
