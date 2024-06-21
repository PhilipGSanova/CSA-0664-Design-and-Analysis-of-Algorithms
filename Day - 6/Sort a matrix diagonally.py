def diagonalSort(mat):
    diagonals = {}
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i - j not in diagonals:
                diagonals[i - j] = []
            diagonals[i - j].append(mat[i][j])
    
    for key in diagonals:
        diagonals[key].sort(reverse=True)
    
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = diagonals[i - j].pop()
    
    return mat

# Example Usage
matrix = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
sorted_matrix = diagonalSort(matrix)
print(sorted_matrix)
