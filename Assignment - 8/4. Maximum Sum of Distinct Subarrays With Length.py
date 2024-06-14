def max_sum_of_distinct_subarrays(nums, k):
    if len(nums) < k:
        return 0
    
    n = len(nums)
    max_sum = 0
    current_sum = 0
    window_start = 0
    element_set = set()
    
    for window_end in range(n):
        while nums[window_end] in element_set:
            element_set.remove(nums[window_start])
            current_sum -= nums[window_start]
            window_start += 1
        
        element_set.add(nums[window_end])
        current_sum += nums[window_end]
        
        if window_end - window_start + 1 == k:
            max_sum = max(max_sum, current_sum)
            element_set.remove(nums[window_start])
            current_sum -= nums[window_start]
            window_start += 1
    
    return max_sum

nums1 = [1, 5, 4, 2, 9, 9, 9]
k1 = 3
print(max_sum_of_distinct_subarrays(nums1, k1))