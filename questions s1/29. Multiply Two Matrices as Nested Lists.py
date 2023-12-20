"""
	Write a program to multiply two matrices as nested lists. 
"""

def multiply_matrices(matrix1, matrix2):
    result_matrix = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return result_matrix

# Example matrices
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[6, 2, 3], [3, 1, 4], [2, 5, 1]]

result = multiply_matrices(matrix1, matrix2)
print("Result Matrix:")
for row in result:
    print(row)
    
"""
	------- output -------
    Result Matrix:
    [18, 19, 14]
    [51, 43, 38]
    [84, 67, 62]
"""