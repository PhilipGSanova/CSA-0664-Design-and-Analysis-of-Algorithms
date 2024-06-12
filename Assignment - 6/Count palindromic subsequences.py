def countPalindromicSubsequences(s: str) -> int:
    MOD = 10 ** 9 + 7
    n = len(s)
    dp = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i][ord(s[i]) - ord('0') - 1] = 1

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(4):
                c = chr(ord('a') + k)
                left = i + 1
                right = j - 1
                while left <= right and s[left] != c:
                    left += 1
                while left <= right and s[right] != c:
                    right -= 1

                if left > right:
                    dp[i][j][k] = dp[i + 1][j - 1][0] + 2
                elif left == right:
                    dp[i][j][k] = dp[i + 1][j - 1][0] + 1
                else:
                    dp[i][j][k] = dp[i + 1][j - 1][0] - dp[left + 1][right - 1][0]

                dp[i][j][k] = (dp[i][j][k] + MOD) % MOD

                for p in range(4):
                    dp[i][j][p] += dp[i][j][k]
                    dp[i][j][p] %= MOD

    return sum(dp[0][n - 1]) % MOD


# Test the function with examples
print(countPalindromicSubsequences("103301"))  # Output: 2
print(countPalindromicSubsequences("0000000"))  # Output: 21
print(countPalindromicSubsequences("9999900000"))  # Output: 2