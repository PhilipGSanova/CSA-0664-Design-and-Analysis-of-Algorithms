def first_last(array, last, first, min_index, max_index, target):
    if first > last:
        return min_index, max_index

    mid = (first + last) // 2

    if array[mid] == target:
        if mid == 0 or array[mid - 1] != target:
            min_index = mid
        if mid == len(array) - 1 or array[mid + 1] != target:
            max_index = mid
        min_index, max_index = first_last(array, mid - 1, first, min_index, max_index, target)
        min_index, max_index = first_last(array, last, mid + 1, min_index, max_index, target)
    elif array[mid] < target:
        min_index, max_index = first_last(array, last, mid + 1, min_index, max_index, target)
    else:
        min_index, max_index = first_last(array, mid - 1, first, min_index, max_index, target)

    return min_index, max_index

arr = [5, 7, 7, 8, 8, 10]
target = 4

min_index, max_index = first_last(arr, len(arr) - 1, 0, -1, -1, target)
print(min_index, max_index)