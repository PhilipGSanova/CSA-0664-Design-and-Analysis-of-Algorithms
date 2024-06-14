from math import gcd
from functools import lru_cache

def min_subarrays_in_valid_split(nums):
    n = len(nums)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    @lru_cache(None)
    def gcd_range(l, r):
        result = nums[l]
        for i in range(l + 1, r):
            result = gcd(result, nums[i])
            if result == 1:
                return 1
        return result
    
    for j in range(1, n + 1):
        for i in range(j):
            if gcd(nums[i], nums[j - 1]) > 1:
                dp[j] = min(dp[j], dp[i] + 1)
    
    return dp[n] if dp[n] != float('inf') else -1

nums1 = [2, 6, 3, 4, 3]
print(min_subarrays_in_valid_split(nums1))