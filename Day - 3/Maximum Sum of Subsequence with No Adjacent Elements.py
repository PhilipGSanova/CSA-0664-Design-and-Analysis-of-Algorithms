def maxSum(nums, queries):
    MOD = 10**9 + 7
    dp = [0] * len(nums)
    
    for i, (pos, val) in enumerate(queries):
        nums[pos] = val
        for j in range(len(nums)):
            if j < 2:
                dp[j] = max(0, nums[j])
            else:
                dp[j] = max(dp[j-1], dp[j-2] + nums[j])
    
    return sum(dp) % MOD


nums = [1, 2, 3, 4, 5]
queries = [[0, 4], [1, 3], [2, 5]]
result = maxSum(nums, queries)
print(result)
