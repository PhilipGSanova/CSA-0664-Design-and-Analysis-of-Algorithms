def mergesort(a,l,r):
    if l<r:
        mid=(l+r)//2
        mergesort(a,l,mid)
        mergesort(a,mid+1,r)
        merger(a,l,mid,r)
def merger(a,l,mid,r):
    L=a[l:mid+1]
    R=a[mid+1:r+1]
    i,j,k=0,0,l

    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            a[k]=L[i]
            i+=1
        else:
            a[k]=R[j]
            j+=1
        k+=1

    while i<len(L):
        a[k]=L[i]
        i+=1
        k+=1
    while j<len(R):
        a[k]=R[j]
        j+=1
        k+=1
a=[11,12,3,4]
mergesort(a,0,3)
print(a)