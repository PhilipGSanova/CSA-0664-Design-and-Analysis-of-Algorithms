def karatsuba(x,y):
    if x<10 or y<10:
        return x*y
    n=max(len(str(x)),len(str(y)))
    m=n//2
    high1,low1=divmod(x,10**m)
    high2,low2=divmod(y,10**m)

    
    c0=karatsuba(low1,low2)
    c1=karatsuba((high1+low1),(high2+low2))
    c2=karatsuba(high1,high2)

    return (c2*(10**(2*m)))+((c1-c2-c0)*(10**m))+c0

x=42
y=34
print(karatsuba(x,y))