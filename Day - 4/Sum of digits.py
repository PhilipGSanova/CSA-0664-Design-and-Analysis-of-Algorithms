def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Test the function
number = 12345
print(f"The sum of digits in {number} is: {sum_of_digits(number)}")
