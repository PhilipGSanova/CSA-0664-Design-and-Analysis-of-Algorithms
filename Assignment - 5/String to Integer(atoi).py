def my_atoi(s: str) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    i = 0
    n = len(s)
    while i < n and s[i].isspace():
        i += 1

    sign = 1
    if i < n and (s[i] == '+' or s[i] == '-'):
        sign = -1 if s[i] == '-' else 1
        i += 1

    result = 0
    while i < n and s[i].isdigit():
        digit = int(s[i])
        
        # Check for overflow
        if result > (INT_MAX - digit) // 10:
            return INT_MAX if sign == 1 else INT_MIN
        
        result = result * 10 + digit
        i += 1

    return sign * result

s1 = "42"
print("String to Integer:", my_atoi(s1))  

s2 = "   -42"
print("String to Integer:", my_atoi(s2))

s3 = "4193 with words"
print("String to Integer:", my_atoi(s3)) 

s4 = "words and 987"
print("String to Integer:", my_atoi(s4))  

s5 = "-91283472332"
print("String to Integer:", my_atoi(s5)) 