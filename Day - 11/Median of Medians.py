def median_of_medians(arr, i):
    def select(arr, left, right, n):
        sublists = [arr[j:j + 5] for j in range(left, right + 1, 5)]

        medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
        
        if len(medians) <= 5:
            pivot = sorted(medians)[len(medians) // 2]
        else:
            pivot = median_of_medians(medians, len(medians) // 2)

        low = [j for j in arr if j < pivot]
        high = [j for j in arr if j > pivot]
        k = len(low)
        
        if i < k:
            return select(low, 0, k - 1, i)
        elif i > k:
            return select(high, 0, len(high) - 1, i - k - 1)
        else:
            return pivot

    return select(arr, 0, len(arr) - 1, i)

arr = [12, 3, 5, 7, 4, 19, 26]
k = 3
print(f"The {k+1}th smallest element is {median_of_medians(arr, k)}")
