def sort_array_by_parity(nums):
    nums.sort(key=lambda x: (x % 2, x % 2 == 0))
    return nums
