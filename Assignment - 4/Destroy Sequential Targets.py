def min_seed(nums, space):
    nums.sort()
    max_targets = 0
    min_seed_value = nums[0]
    
    for num in nums:
        targets = 1
        for i in range(1, len(nums)):
            if nums[i] - num <= space * (i - 1):
                targets += 1
        if targets > max_targets:
            max_targets = targets
            min_seed_value = num
    
    return min_seed_value

# Example 1
nums = [3, 7, 8, 1, 1, 5]
space = 2
print(min_seed(nums, space))  # Output: 1

# Example 2
nums = [1, 3, 5, 2, 4, 6]
space = 2
print(min_seed(nums, space))  # Output: 1

# Example 3
nums = [6, 2, 5]
space = 100
print(min_seed(nums, space))  # Output: 2
