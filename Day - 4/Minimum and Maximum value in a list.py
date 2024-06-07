def min_max_sequence(numbers):
    for num_list in numbers:
        print(f"List: {num_list}")
        print(f"Minimum Value: {min(num_list)}")
        print(f"Maximum Value: {max(num_list)}")
        print()
        
# Example Usage
numbers_list = [[3, 7, 1, 9], [5, 2, 8, 4], [11, 6, 10]]
min_max_sequence(numbers_list)
