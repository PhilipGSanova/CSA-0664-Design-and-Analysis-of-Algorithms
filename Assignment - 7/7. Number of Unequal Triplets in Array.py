def countUnequalTriplets(nums):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                    count += 1
    return count

nums1 = [4, 4, 2, 4, 3]
print(countUnequalTriplets(nums1)) 