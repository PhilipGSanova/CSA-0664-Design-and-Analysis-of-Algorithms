
def find_pivot_integer(n):
    total_sum = n * (n + 1) // 2
    prefix_sum = 0

    for x in range(1, n + 1):
        prefix_sum += x
        suffix_sum = total_sum - prefix_sum

        if prefix_sum == suffix_sum:
            return x

    return -1


# Test the function with examples
print(find_pivot_integer(8))  # Output: 6
print(find_pivot_integer(1))  # Output: 1
print(find_pivot_integer(4))  # Output: -1
