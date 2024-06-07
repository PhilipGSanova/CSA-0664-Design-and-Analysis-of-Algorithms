def is_perfect_number(num):
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    return sum_divisors == num

def find_perfect_numbers(limit):
    perfect_numbers = []
    for i in range(1, limit + 1):
        if is_perfect_number(i):
            perfect_numbers.append(i)
    return perfect_numbers

limit = 10000
perfect_numbers = find_perfect_numbers(limit)
print("Perfect numbers up to", limit, "are:", perfect_numbers)
