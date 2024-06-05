def max_diff(num):
    s = str(num)
    a = int(s.replace(max(s), '9'))
    b = int(s.replace(min(s), '1'))
    return a - b

# Test the function with the examples
print(max_diff(555))  # Output: 888
print(max_diff(9))    # Output: 8
