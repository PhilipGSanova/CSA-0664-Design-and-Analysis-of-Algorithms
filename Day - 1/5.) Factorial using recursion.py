def fact(n):
    if n == 0:
        return 1
    else:
        return fact(n-1)*n
    
n = 4

print("The factorial of",n,"is",fact(n))