def min_beautiful_number(n, target):
    digit_sum = sum(int(digit) for digit in str(n))
    x = max(0, (target - digit_sum) // 9) * 9
    return x

# Test the function with examples
print(min_beautiful_number(16, 6))  # Output: 4
print(min_beautiful_number(467, 6))  # Output: 33
print(min_beautiful_number(1, 1))  # Output: 0
