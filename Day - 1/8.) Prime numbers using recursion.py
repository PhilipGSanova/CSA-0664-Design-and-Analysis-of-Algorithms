def prime(n, i=2):
    if n <= 2:
        return True if n == 2 else False
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return prime(n, i + 1)

def generate_primes(n):
    if n > 1:
        generate_primes(n - 1)
        if prime(n):
            print(n)

generate_primes(20)