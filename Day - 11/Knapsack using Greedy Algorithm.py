def knapsack_greedy(values, weights, capacity):
    n = len(values)
    indexes = list(range(n))
    ratios = [(values[i] / weights[i], i) for i in range(n)]
    ratios.sort(reverse=True)
    
    max_value = 0
    knapsack = [0] * n
    
    for ratio, i in ratios:
        if weights[i] <= capacity:
            knapsack[i] = 1
            max_value += values[i]
            capacity -= weights[i]
        else:
            fraction = capacity / weights[i]
            knapsack[i] = fraction
            max_value += values[i] * fraction
            break
    
    return max_value, knapsack

# Example Usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
max_val, items_in_knapsack = knapsack_greedy(values, weights, capacity)
print("Maximum value:", max_val)
print("Items in knapsack:", items_in_knapsack)
