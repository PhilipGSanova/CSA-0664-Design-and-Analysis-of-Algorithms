def beautiful_integer(n, target):
    digit_sum = sum(int(digit) for digit in str(n))
    if digit_sum <= target:
        return 0
    
    x = 0
    while True:
        if sum(int(digit) for digit in str(n + x)) <= target:
            return x
        x += 1
