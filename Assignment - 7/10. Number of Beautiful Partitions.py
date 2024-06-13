def is_prime_digit(ch):
    return ch in {'2', '3', '5', '7'}

def is_non_prime_digit(ch):
    return ch in {'1', '4', '6', '8', '9'}

def beautiful_partitions(s, k, minLength):
    MOD = 10**9 + 7
    n = len(s)
    
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(k):
            if dp[i][j] > 0:
                for l in range(i + minLength, n + 1):
                    if is_prime_digit(s[i]) and is_non_prime_digit(s[l - 1]):
                        dp[l][j + 1] = (dp[l][j + 1] + dp[i][j]) % MOD

    return dp[n][k]

s1 = "23542185131"
k1 = 3
minLength1 = 2
print(beautiful_partitions(s1, k1, minLength1))