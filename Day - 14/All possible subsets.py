from itertools import combinations

def subsets(nums):
    res = []
    for i in range(len(nums)+1):
        res += list(combinations(nums, i))
    return [list(subset) for subset in res]

# Example 1
nums1 = [1, 2, 3]
print(subsets(nums1))

# Example 2
nums2 = [0]
print(subsets(nums2))
