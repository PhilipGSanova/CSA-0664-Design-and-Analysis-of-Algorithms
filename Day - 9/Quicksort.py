def quicksort(a,l,r):
    if l<r:
        index=partition(a,l,r)
        quicksort(a,l,index)
        quicksort(a,index+1,r)
def partition(a,l,r):
    i=l+1
    j=r
    while True:
        while i<=j and a[i]<=a[l]:
            i+=1
        while i<=j and a[j]>=a[l]:
            j-=1
        if i<=j:
            a[i],a[j]=a[j],a[i]
        else:
            break
    a[l],a[j]=a[j],a[l]
    return j

a=[11,12,3,4]
quicksort(a,0,3)
print(a)