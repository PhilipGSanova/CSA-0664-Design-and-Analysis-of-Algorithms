def small_string(s, arr, n):
    parent = {i: i for i in range(len(s))}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        parent[find(x)] = find(y)

    for a, b in arr:
        union(a, b)

    groups = {}
    for i, c in enumerate(s):
        root = find(i)
        if root not in groups:
            groups[root] = []
        groups[root].append(c)

    for group in groups.values():
        group.sort()

    result = []
    for i in range(len(s)):
        root = find(i)
        result.append(groups[root].pop(0))

    return ''.join(result)

s = "bad"
arr = [[0, 2]]
n = len(arr)
print(small_string(s, arr, n))
