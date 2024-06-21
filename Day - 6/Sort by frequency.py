def frequency_sort(s):
    char_freq = {}
    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    sorted_chars = sorted(char_freq, key=lambda x: (-char_freq[x], x))
    sorted_str = ''.join([char * char_freq[char] for char in sorted_chars])
    return sorted_str

# Test the function with examples
print(frequency_sort("tree"))  # Output: "eert" or "eetr"
print(frequency_sort("cccaaa"))  # Output: "aaaccc" or "cccaaa"
print(frequency_sort("Aabb"))  # Output: "bbAa" or "bbaA"
