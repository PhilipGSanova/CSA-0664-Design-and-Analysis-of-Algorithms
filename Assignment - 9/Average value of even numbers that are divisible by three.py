def average_even_divisible_by_3(nums):
    even_divisible_by_3 = [num for num in nums if num % 2 == 0 and num % 3 == 0]
    if not even_divisible_by_3:
        return 0
    return sum(even_divisible_by_3) // len(even_divisible_by_3)

# Example 1
nums1 = [1, 3, 6, 10, 12, 15]
print(average_even_divisible_by_3(nums1))  # Output: 9

# Example 2
nums2 = [1, 2, 4, 7, 10]
print(average_even_divisible_by_3(nums2))  # Output: 0
