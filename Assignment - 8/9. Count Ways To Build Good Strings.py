def count_good_strings(low, high, zero, one):
    MOD = 10**9 + 7
    
    dp = [0] * (high + 1)
    dp[0] = 1    
    for i in range(1, high + 1):
        if i >= zero:
            dp[i] += dp[i - zero]
        if i >= one:
            dp[i] += dp[i - one]
        dp[i] %= MOD
    
    result = sum(dp[low:high + 1]) % MOD
    
    return result

low1, high1, zero1, one1 = 3, 3, 1, 1
print(count_good_strings(low1, high1, zero1, one1))