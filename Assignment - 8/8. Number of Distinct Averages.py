def distinct_averages(nums):
    nums.sort()
    
    averages = set()
    
    i, j = 0, len(nums) - 1
    
    while i < j:
        avg = (nums[i] + nums[j]) / 2
        averages.add(avg)
        i += 1
        j -= 1
    
    return len(averages)

nums1 = [4, 1, 4, 0, 3, 5]
print(distinct_averages(nums1))