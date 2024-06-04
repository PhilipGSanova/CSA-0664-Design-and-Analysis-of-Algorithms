def prime(n, i=2):
    if n == i:
        return True
    elif n % i == 0:
        return False
    return prime(n, i + 1)


n = 971

if prime(n):
    print("Yes,", n, "is Prime")
else:
    print("No,", n, "is not a Prime")