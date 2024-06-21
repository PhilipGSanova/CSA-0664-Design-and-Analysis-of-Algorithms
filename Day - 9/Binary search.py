def binsearch(a,i,j,k):
    if i<j:
        mid=(i+j)//2
        if a[mid]==k:
            return mid
        elif a[mid] < k:
            return binsearch(a,i,mid,k)
        else:
            return binsearch(a,mid+1,j,k)
    return -1
a=[11,12,3,4]
k=31
print(binsearch(a,0,len(a)-1,k))