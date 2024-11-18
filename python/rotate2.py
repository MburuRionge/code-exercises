def rotate_matrix(matrix):
    n = len(matrix)
    
    #step1 transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    #step 2 reverse each row
    for row in matrix:
        row.reverse()

# 4x4 matrix
matrix_4x4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

rotate_matrix(matrix_4x4)
print("Rotated 4x4 matrix:")
for row in matrix_4x4:
    print(row)