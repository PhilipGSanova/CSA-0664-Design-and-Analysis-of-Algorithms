def check_if_can_break(s1, s2):
    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)
    
    return all(s1_char >= s2_char for s1_char, s2_char in zip(s1_sorted, s2_sorted)) or all(s1_char <= s2_char for s1_char, s2_char in zip(s1_sorted, s2_sorted))

# Test the function with examples
print(check_if_can_break("abc", "xya"))  # Output: True
print(check_if_can_break("abe", "acd"))  # Output: False
print(check_if_can_break("leetcodee", "interview"))  # Output: True
