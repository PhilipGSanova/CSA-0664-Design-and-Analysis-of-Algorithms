def reverse_integer(x: int) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    result = 0
    negative = x < 0
    x = abs(x)
    
    while x != 0:
        pop = x % 10
        x //= 10
        
        if result > (INT_MAX - pop) // 10:
            return 0
        
        result = result * 10 + pop
    
    if negative:
        result = -result
    
    return result if INT_MIN <= result <= INT_MAX else 0

num = 123
print("Reversed integer is:", reverse_integer(num))  

num = -123
print("Reversed integer is:", reverse_integer(num))  

num = 1534236469
print("Reversed integer is:", reverse_integer(num))  