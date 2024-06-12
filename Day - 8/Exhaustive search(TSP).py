def exhaustive_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

# Example Usage
data_list = [4, 7, 2, 9, 1, 5]
target_value = 9
result = exhaustive_search(data_list, target_value)
print(f"Target value {target_value} found at index: {result}")
