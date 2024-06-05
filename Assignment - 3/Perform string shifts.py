def stringShift(s, shift):
    total_shift = 0
    for sh in shift:
        if sh[0] == 0:
            total_shift -= sh[1]
        else:
            total_shift += sh[1]
    total_shift %= len(s)
    return s[-total_shift:] + s[:-total_shift]

# Example 1
s = "abc"
shift = [[0,1],[1,2]]
print(stringShift(s, shift))

# Example 2
s = "abcdefg"
shift = [[1,1],[1,1],[0,2],[1,3]]
print(stringShift(s, shift))