def karat(x,y):
    if x<10 or y<10:
        return x*y
    
    m=max(len(str(x)),len(str(y)))
    n=m//2

    h1,l1=divmod(x,10**n)
    h2,l2=divmod(y,10**n)

    c0=karat(l1,l2)
    c1=karat((h1+l1),(h2,l2))
    c2=karat(h1,h2)

    return (c2*(10**(2*n)))+((c1-c2-c0)*(10**n))+c0