def count_elements(arr):
    return sum(1 for x in arr if x + 1 in arr)

# Example 1
arr1 = [1, 2, 3]
output1 = count_elements(arr1)
print(output1)  # Output: 2

# Example 2
arr2 = [1, 1, 3, 3, 5, 5, 7, 7]
output2 = count_elements(arr2)
print(output2)  # Output: 0
