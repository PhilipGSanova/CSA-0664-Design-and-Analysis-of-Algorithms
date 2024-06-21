def sort(arr):
    n=len(arr)
    red=0
    white=0
    blue=0
    for i in range(n):
        if arr[i]==0:
            red+=1
        elif arr[i]==1:
            white+=1
        else:
            blue+=1
    
    arr=[0]*red + [1]*white + [2]*blue
    return arr

arr=[2,0,2,1,1,0]
arr=sort(arr)
print(arr)