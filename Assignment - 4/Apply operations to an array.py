def shift_zeros(nums):
    n = len(nums)
    for i in range(n - 1):
        if nums[i] == nums[i + 1]:
            nums[i] *= 2
            nums[i + 1] = 0
    nums.sort(key=lambda x: x == 0)
    return nums

# Example 1
nums1 = [1, 2, 2, 1, 1, 0]
output1 = shift_zeros(nums1)
print(output1)

# Example 2
nums2 = [0, 1]
output2 = shift_zeros(nums2)
print(output2)
