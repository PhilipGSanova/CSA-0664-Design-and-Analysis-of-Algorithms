def remove_letters(s):
    for char in sorted(set(s)):
        s = s.replace(char, '', 1)
    return s

s = "aabcbbca"
result = remove_letters(s)
print(result)
