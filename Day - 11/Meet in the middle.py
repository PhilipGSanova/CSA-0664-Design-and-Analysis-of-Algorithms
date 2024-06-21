from itertools import combinations

def subset_sums(arr):
    """ Helper function to compute all possible subset sums of a list """
    sums = []
    for i in range(len(arr) + 1):
        for combo in combinations(arr, i):
            sums.append(sum(combo))
    return sums

def meet_in_the_middle(arr, target):
    """ Main function implementing the 'Meet in the Middle' approach """
    n = len(arr)
    
    # Split the array into two halves
    left_half = arr[:n//2]
    right_half = arr[n//2:]
    
    # Compute all possible subset sums for each half
    left_sums = subset_sums(left_half)
    right_sums = subset_sums(right_half)
    
    # Use a set for quick lookup of right_half sums
    right_sums_set = set(right_sums)
    
    # Check if there is a pair of subset sums that add up to the target
    for left_sum in left_sums:
        if (target - left_sum) in right_sums_set:
            return True
    
    return False

# Example usage:
arr = [3, 34, 4, 12, 5, 2]
target = 9
print(f"Is there a subset with the target sum {target}? {'Yes' if meet_in_the_middle(arr, target) else 'No'}")
