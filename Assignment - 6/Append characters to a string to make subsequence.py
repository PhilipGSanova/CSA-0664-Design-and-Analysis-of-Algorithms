def min_append_to_make_subsequence(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            j += 1
        i += 1
    return len(t) - j

# Example 1
s1 = "coaching"
t1 = "coding"
print(min_append_to_make_subsequence(s1, t1))  # Output: 4

# Example 2
s2 = "abcde"
t2 = "a"
print(min_append_to_make_subsequence(s2, t2))  # Output: 0

# Example 3
s3 = "z"
t3 = "abcde"
print(min_append_to_make_subsequence(s3, t3))  # Output: 5