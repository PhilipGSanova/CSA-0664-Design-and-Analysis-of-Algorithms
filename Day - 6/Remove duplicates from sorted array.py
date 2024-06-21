def remove(array):
    m = 0
    for i in range(1, len(array)):
        if array[i] != array[m]:
            m += 1
            array[m] = array[i]
    return array, m + 1

array = [1, 1, 2, 3, 3, 4, 4, 5, 5, 5, 5, 6]
array, m = remove(array)
print(m)
print(array)
