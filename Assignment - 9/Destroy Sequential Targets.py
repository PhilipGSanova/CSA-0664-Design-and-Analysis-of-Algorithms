def min_value_to_destroy_targets(nums, space):
    max_targets = 0
    min_value = float('inf')
    
    for num in nums:
        targets = sum(1 for i in range(num, max(nums)+space, space) if i in nums)
        if targets > max_targets or (targets == max_targets and num < min_value):
            max_targets = targets
            min_value = num
    
    return min_value

# Example
nums = [3, 7, 8, 1, 1, 5]
space = 2
output = min_value_to_destroy_targets(nums, space)
print(output)  # Output: 1
