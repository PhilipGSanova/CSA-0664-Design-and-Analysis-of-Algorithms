def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)
    return [candy + extraCandies >= max_candies for candy in candies]

# Example 1
candies1 = [2, 3, 5, 1, 3]
extraCandies1 = 3
output1 = kidsWithCandies(candies1, extraCandies1)
print(output1)  # Output: [True, True, True, False, True]

# Example 2
candies2 = [4, 2, 1, 1, 2]
extraCandies2 = 1
output2 = kidsWithCandies(candies2, extraCandies2)
print(output2)  # Output: [True, False, False, False, False]

# Example 3
candies3 = [12, 1, 12]
extraCandies3 = 10
output3 = kidsWithCandies(candies3, extraCandies3)
print(output3)  # Output: [True, False, True]
