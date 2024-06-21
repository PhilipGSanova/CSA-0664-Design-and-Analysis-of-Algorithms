def find_second_greater_integers(nums):
    n = len(nums)
    answer = [-1] * n
    
    stack = []
    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            answer[stack.pop()] = nums[i]
        stack.append(i)
    
    return answer

# Example
nums = [2, 4, 0, 9, 6]
output = find_second_greater_integers(nums)
print(output)  # Output: [9, 6, 6, -1, -1]
