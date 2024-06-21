def merge_sorted(arr1,arr2):
    arr3=[j for j in arr1 if j!=0] + [m for m in arr2 if m!=0]
    arr3=sorted(arr3)
    return arr3
arr1=[1,2,3,0,0,0]
arr2=[2,5,6]
arr3=merge_sorted(arr1,arr2)
print(arr3)