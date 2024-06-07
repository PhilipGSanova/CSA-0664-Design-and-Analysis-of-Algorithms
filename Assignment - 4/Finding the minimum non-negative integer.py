def min_non_negative_integer(n, target):
    digit_sum = sum(int(digit) for digit in str(n))
    if digit_sum <= target:
        return 0
    else:
        return (target - digit_sum % (target + 1)) + n

# Test Examples
print(min_non_negative_integer(16, 6))  # Output: 4
print(min_non_negative_integer(467, 6))  # Output: 33
print(min_non_negative_integer(1, 1))    # Output: 0
