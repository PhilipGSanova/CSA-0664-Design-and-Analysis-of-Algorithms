# Master Theorem
def master_theorem(a, b, k):
    if a > b ** k:
        return "T(n) = Θ(n^log_{%d}(%d))" % (b, a)
    elif a == b ** k:
        return "T(n) = Θ(n^log_{%d}(%d) * log(n))" % (b, a)
    else:
        return "T(n) = Θ(n^%d)" % k

# Example
print(master_theorem(3, 2, 1))

# Substitution Method
def substitution_method(T, n):
    if n == 0:
        return 1
    else:
        return 2 * substitution_method(T, n-1) + 1

# Example
print(substitution_method(1, 3))

# Iteration Method
def iteration_method(a, b, n):
    result = a
    for i in range(1, n):
        result = b * result + 1
    return result

# Example
print(iteration_method(1, 2, 3))
