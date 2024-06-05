def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Test the functions with sample inputs
arr = [2, 4, 6, 8, 10]
target = 6
print("Linear Search Result:", linear_search(arr, target))

arr.sort()
print("Binary Search Result:", binary_search(arr, target))

n = 5
print("Factorial of", n, "is", factorial(n))
