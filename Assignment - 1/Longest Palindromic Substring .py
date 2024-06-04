def longest_palindromic_substring(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""
    
    dp = [[False] * n for _ in range(n)]
    
    start = 0
    max_length = 1
    for i in range(n):
        dp[i][i] = True
    

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2
    
    
    for k in range(3, n + 1):  
        for i in range(n - k + 1):
            j = i + k - 1 
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if k > max_length:
                    start = i
                    max_length = k
    
    return s[start:start + max_length]

s = "babad"
print("Longest Palindromic Substring is:", longest_palindromic_substring(s))