import math
from math import gcd
from functools import reduce

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def lcm_list(numbers):
    return reduce(lcm, numbers)

def count_subarrays_with_lcm_k(nums, k):
    n = len(nums)
    count = 0
    
    for i in range(n):
        current_lcm = nums[i]
        if current_lcm == k:
            count += 1
        for j in range(i + 1, n):
            current_lcm = lcm(current_lcm, nums[j])
            if current_lcm == k:
                count += 1
            elif current_lcm > k:
                break
                
    return count

nums1 = [3, 6, 2, 7, 1]
k1 = 6
print(count_subarrays_with_lcm_k(nums1, k1)) 
nums2 = [3]
k2 = 2
print(count_subarrays_with_lcm_k(nums2, k2)) 