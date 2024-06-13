def maxPalindromicSubstrings(s, k):
    n = len(s)
    if k > n:
        return 0
    
    is_palindrome = [[False] * n for _ in range(n)]
    
    for i in range(n):
        is_palindrome[i][i] = True
    
    for i in range(n - 1):
        is_palindrome[i][i + 1] = (s[i] == s[i + 1])
    
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            is_palindrome[i][j] = (s[i] == s[j]) and is_palindrome[i + 1][j - 1]
    
    count = 0
    i = 0
    while i <= n - k:
        found = False
        for j in range(i + k - 1, n):
            if is_palindrome[i][j]:
                count += 1
                i = j + 1
                found = True
                break
        if not found:
            i += 1
    
    return count

s1 = "abaccdbbd"
k1 = 3
print(maxPalindromicSubstrings(s1, k1))

s2 = "adbcda"
k2 = 2
print(maxPalindromicSubstrings(s2, k2))