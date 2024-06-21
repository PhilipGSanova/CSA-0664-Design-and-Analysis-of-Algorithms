def max_chunks_to_make_sorted(arr):
    chunks = 0
    max_val = 0
    for i, val in enumerate(arr):
        max_val = max(max_val, val)
        if max_val == i:
            chunks += 1
    return chunks

# Example 1
arr1 = [4, 3, 2, 1, 0]
print(max_chunks_to_make_sorted(arr1))  # Output: 1

# Example 2
arr2 = [1, 0, 2, 3, 4]
print(max_chunks_to_make_sorted(arr2))  # Output: 4
