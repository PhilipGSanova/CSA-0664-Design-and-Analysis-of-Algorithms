from collections import Counter

def min_value_string(s):
    def cost(i, t):
        return sum(1 for j in range(i) if t[j] == t[i])

    def value(t):
        return sum(cost(i, t) for i in range(len(t)))

    letters = 'abcdefghijklmnopqrstuvwxyz'
    min_value = float('inf')
    result = ''

    for c in letters:
        t = s.replace('?', c)
        curr_value = value(t)
        if curr_value < min_value:
            min_value = curr_value
            result = t

    return result

# Example
s = "a?b?c?"
result = min_value_string(s)
print(result)
