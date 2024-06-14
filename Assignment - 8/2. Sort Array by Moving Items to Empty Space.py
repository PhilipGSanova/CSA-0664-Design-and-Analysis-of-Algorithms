def min_operations_to_sort(nums):
    n = len(nums)
    visited = [False] * n
    zero_index = nums.index(0)
    swaps = 0

    for i in range(n):
        if not visited[i] and nums[i] != i:
            cycle_length = 0
            x = i
            while not visited[x]:
                visited[x] = True
                x = nums[x]
                cycle_length += 1
            if cycle_length > 0:
                swaps += cycle_length - 1

    if zero_index == 0 or zero_index == n - 1:
        return swaps
    else:
        return swaps + 1

nums = [4, 2, 0, 3, 1]
print(min_operations_to_sort(nums))
