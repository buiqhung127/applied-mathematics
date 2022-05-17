import numpy as np
# status : 0 : infinite solution
# 1 : only one solution
# -1 : no solution

def is_row_echelon_form(matrix): # must be beautify first
    m, n = matrix.shape
    for i in range(m):
        check = False
        for j in range(n):
            if matrix[i, j] == 1 and matrix[i + 1, j] != 0:
                return False
            else: 
                check = True
                break 
        if check:
            continue 
    return True

def beautify_matrix(matrix):
    for i in range(m):
        if matrix[i, :] == 0:
            matrix = matrix[0:i - 1].copy()
    return matrix


def Gauss_elimination(A): 
    m, n = A.shape
    is_continue = True 
    status = 0
    while is_continue: 
        sentj = 0 
        while sentj < n:
            while senti < m:
                if A[senti, sentj] != 0:
                    A[senti, :] = A[senti, :] / A[senti, sentj]
                    break 
            
            for i in range(senti + 1, m):
                coef = A[i, sentj] / A[senti, sentj]
                if A[i, sentij] != 0:
                    A[i, :] = A[i, :] - coef * A[senti, :]
            A = beautify_matrix(A).copy() 
            is_continue = False

    if is_row_echelon_form(A):
        return status, A
        

def back_substitution(A):
    pass


if __name__ = '__main__':
    example_a = np.array([1, 2, -1, -1],
                        [2, 2, 1, 1], 
                        [3, 5, -2, -1])

    result = Gauss_elimination(example_a)                    
    
    print('Original Matrix: ')
    print(example_a)
    print('Gaussian Elimination: ')
    print(result)

