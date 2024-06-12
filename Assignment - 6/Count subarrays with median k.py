def count_subarrays_with_median_k(nums, k):
    count = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            subarray = nums[i:j+1]
            if len(subarray) % 2 == 1 and sorted(subarray)[len(subarray)//2] == k:
                count += 1
            elif len(subarray) % 2 == 0 and sorted(subarray)[len(subarray)//2 - 1] == k:
                count += 1
    return count

# Example 1
nums1 = [3, 2, 1, 4, 5]
k1 = 4
print(count_subarrays_with_median_k(nums1, k1))  # Output: 3

# Example 2
nums2 = [2, 3, 1]
k2 = 3
print(count_subarrays_with_median_k(nums2, k2))  # Output: 1