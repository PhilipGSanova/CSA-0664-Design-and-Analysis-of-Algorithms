def find_second_greater(nums):
    answer = []
    for i in range(len(nums)):
        found = False
        for j in range(i+1, len(nums)):
            if nums[j] > nums[i]:
                for k in range(j+1, len(nums)):
                    if nums[k] > nums[i]:
                        answer.append(nums[k])
                        found = True
                        break
                if not found:
                    answer.append(-1)
                break
        if not found:
            answer.append(-1)
    return answer

# Test the function with examples
nums1 = [2, 4, 0, 9, 6]
nums2 = [3, 3]

output1 = find_second_greater(nums1)
output2 = find_second_greater(nums2)

print(output1)  # Output: [9, 6, 6, -1, -1]
print(output2)  # Output: [-1, -1]
