def insert_number_in_list(lst, num, index):
    lst.insert(index, num)
    return lst

# Example Usage
my_list = [1, 2, 3, 4, 5]
number_to_insert = 10
insertion_index = 2
result_list = insert_number_in_list(my_list, number_to_insert, insertion_index)
print(result_list)
