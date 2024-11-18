def rotate_matrix(matrix):
    """
    rotates an n x n matrix on a 90 degrees clockwise in place
    :param matrix: List[List[int]] - 2D square matrix
    :retuen: None (matrix is modified in place)
    """
    n = len(matrix)

    #step 1 transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    #step 2 reverse each row
    for row in matrix:
        row.reverse()

#example 1
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotate_matrix(matrix)
print(matrix)    