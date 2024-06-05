# Non-Recursive Algorithm
def non_recursive_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Recursive Algorithm
def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)

# Test the Algorithms
number = 5
print(f"Non-Recursive Factorial of {number}: {non_recursive_factorial(number)}")
print(f"Recursive Factorial of {number}: {recursive_factorial(number)}")
