def isPalindrome(x: int)->bool:
    if x < 0:
        return False
    s = str(x)
    return s == s[::-1]
print(isPalindrome(10))
print(isPalindrome(101))