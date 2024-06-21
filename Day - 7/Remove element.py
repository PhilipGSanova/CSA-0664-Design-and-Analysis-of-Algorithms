def remove(a,t):
    k=0
    for i in range(len(a)):
        if a[i]==t:
            a[i]=a[i]-1
            k+=1
    for j in range(0,k):
        a[j]=k
    return a

a=[1,2,3,2,3]
t=2
a=remove(a,t)
print(a)