def rotate_matrix(matrix):
    """
    rotates for a 90 degrees
    """
    
    n = len(matrix)
    
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    for row in matrix:
        row.reverse()
        
matrix_5x5 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

rotate_matrix(matrix_5x5)
print("\nRotated 5x5 Matrix:")
for row in matrix_5x5:
    print(row)