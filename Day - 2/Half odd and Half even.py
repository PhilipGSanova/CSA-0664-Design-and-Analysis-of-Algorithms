nums = [1, 2, 3, 4, 5, 6]
half_odd_even = [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 != 0]
print(half_odd_even)
