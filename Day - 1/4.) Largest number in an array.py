def max(array,n):
    max_val=array[0]
    for i in range(1,n):
        if max_val < array[i]:
            max_val = array[i]
    return max_val

array=[1,2,3,4,5]
n=5

print("The largest element in the given array is",max(array,n))