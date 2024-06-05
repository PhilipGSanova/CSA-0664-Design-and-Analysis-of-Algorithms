def reverse_number(n, rev=0):
    if n == 0:
        return rev
    else:
        return reverse_number(n // 10, rev * 10 + n % 10)

# Input number
number = 12345

# Call the function to find the reverse of the number
reverse = reverse_number(number)

# Output the reversed number
print(f"The reverse of {number} is: {reverse}")
