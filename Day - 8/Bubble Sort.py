def swap(a,i,j):
    a[i],a[j]=a[j],a[i]
    return 
def bubble(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                swap(a,i,j)
    return a
a=[6,3,2,7,4]
print(bubble(a))