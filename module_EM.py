def matrix_multiply(A, B):
    # check if matrices can be multiplied
    if(len(A[0]) != len(B)):
        raise ValueError("Invalid martrix dimensions")
    
    # initialize result matrix with zeros
    result = [[0 for j in range(len(B[0]))] for i in range(len(A))]

    # recursive multiplication of matrices
    def multiply(A, B, result, i, j, k):
        if i >= len(A):
            return
        if j >= len(B[0]):
            return multiply(A, B, result, i+1, 0, 0)
        if k >= len(B):
            return multiply(A, B, result, i, j+1, 0)
        result[i][j] += A[i][k] * B[k][j]
        multiply(A, B, result, i, j, k+1)

    # perform matrix multiplication
    multiply(A, B, result, 0, 0, 0)
    return result

def show_matrix(matrix, row_size, column_size = 1):
    for row in range(row_size):
        for column in range(column_size):
            print(matrix[row][column], end=" ")
        print()

def cal_EM(result_matrix, row, column, E_matrix, row_size, column_size):
    index_r = row + 1 
    while index_r < row_size:
        if(result_matrix[index_r][column] != 0):
            l = (result_matrix[index_r][column]/result_matrix[row][column])*(-1)
            print("L: " + str(l))
            E_matrix[index_r][column] = l
            show_matrix(E_matrix, row_size, row_size)
            result_matrix = matrix_multiply(E_matrix, result_matrix)
            show_matrix(result_matrix, row_size, column_size)
            print("|")
            E_matrix[index_r][column] = 0
        else:
            pass
        index_r+=1

    return result_matrix

def consistent_check(matrix, pivot, row, column):
    i_row = len(pivot)
    consistent_status = True
    while i_row < row:
        if(matrix[i_row][column-1] != 0):
            for i in matrix[i_row]:
                if(i != 0):
                    consistent_status = True
                    pass
                else:
                    consistent_status = False
                    break
        else:
            consistent_status = True
        i_row+=1
    return consistent_status
