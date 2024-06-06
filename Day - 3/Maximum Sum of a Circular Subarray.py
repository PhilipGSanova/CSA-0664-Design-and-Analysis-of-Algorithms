def maxSubarraySumCircular(nums):
    total_sum = max_sum = min_sum = max_temp = min_temp = nums[0]
    
    for num in nums[1:]:
        max_temp = max(num, max_temp + num)
        max_sum = max(max_sum, max_temp)
        
        min_temp = min(num, min_temp + num)
        min_sum = min(min_sum, min_temp)
        
        total_sum += num
    
    return max(max_sum, total_sum - min_sum) if max_sum > 0 else max(nums)
