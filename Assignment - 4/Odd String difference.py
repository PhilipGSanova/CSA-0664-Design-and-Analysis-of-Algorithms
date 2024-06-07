def find_difference_word(words):
    n = len(words[0])
    for i in range(n - 1):
        diff = ord(words[0][i + 1]) - ord(words[0][i])
    
    for word in words:
        temp_diff = []
        for i in range(n - 1):
            temp_diff.append(ord(word[i + 1]) - ord(word[i]))
        if temp_diff != diff:
            return word

# Example 1
words1 = ["adc", "wzy", "abc"]
print(find_difference_word(words1))  # Output: "abc"

# Example 2
words2 = ["aaa", "bob", "ccc", "ddd"]
print(find_difference_word(words2))  # Output: "bob"
