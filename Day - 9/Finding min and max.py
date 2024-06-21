def min_max(a,i,j,minval=0,maxval=0):
    if i==j:
        minval=maxval=a[0]
    else:
        if (i==j-1):
            if a[i]<a[j]:
                maxval=a[j]
                minval=a[i]
            else:
                maxval=a[i]
                minval=a[j]
        else:
            mid=(i+j)//2
            min1,max1=min_max(a,i,mid,minval,maxval)
            min2,max2=min_max(a,mid+1,j,minval,maxval)
            if max1<max2:
                maxval=max2
            else:
                maxval=max1
            if min1<min2:
                minval=min1
            else:
                minval=min2
    return minval,maxval
a=[11,12,3,4]
print(min_max(a,0,3))