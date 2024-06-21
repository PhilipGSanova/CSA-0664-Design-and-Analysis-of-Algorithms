def intersection(a,b,c):
    d=list(set(a)&set(b)&set(c))
    d=sorted(d)
    return d
a=[1,2,3,4]
b=[1,2,5,6]
c=[5,6,7,3,2,1]
d=intersection(a,b,c)
print(d)