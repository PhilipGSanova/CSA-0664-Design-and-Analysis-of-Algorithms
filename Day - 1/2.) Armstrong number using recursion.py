def armstrong(num, digit_count):
    if num == 0:
        return 0
    return ((num % 10) ** digit_count) + armstrong(num // 10, digit_count)

def check_armstrong(num):
    digit_count = len(str(num))
    return num == armstrong(num, digit_count)

number = 371
print(check_armstrong(number))