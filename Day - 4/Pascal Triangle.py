def generate_pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [None for _ in range(i + 1)]
        row[0], row[-1] = 1, 1
        for j in range(1, len(row) - 1):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

def print_pascal_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)).center(len(triangle[-1]) * 2))

n = 5
pascal_triangle = generate_pascal_triangle(n)
print_pascal_triangle(pascal_triangle)
