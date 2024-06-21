def minBeautifulNumber(n, target):
    digit_sum = sum(int(digit) for digit in str(n))
    return max(0, (target - digit_sum) // 9)
    
# Test the function with examples
print(minBeautifulNumber(16, 6))  # Output: 4
print(minBeautifulNumber(467, 6))  # Output: 33
print(minBeautifulNumber(1, 1))  # Output: 0
