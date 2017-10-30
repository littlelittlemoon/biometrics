#-*- coding: UTF-8 -*- 
import numpy as np

M = np.random.randint(1 ,100 ,(100 ,100))     # 生成一个随机矩阵
M_transpose = M.T       # 矩阵M的转置

print('M = ', M)
print('M_transpose = ', M_transpose)

# 计算所给矩阵所有元素之和
def getSumOfTheMatrix(matrix):
    matrix_shape = matrix.shape
    h = matrix_shape[0]
    l = matrix_shape[1]
    sum = 0
    for i in range(0, h):
        for j in range(0, l):
            sum += M[i][j]
    return sum

# 计算所给矩阵指定行和列的元素之和 
def countSumOfTheMatrixSSpecialRowAndColumn(matrix, row, column):
    matrix_shape = matrix.shape
    h = matrix_shape[0]
    l = matrix_shape[1]
    
    if (row > h):
        for i in range(3, 0, -1):
            row = int(input("Please enter right row, you have %d chance(s): " % i))
            if (row <= h):
                break
    if (column > l):
        for i in range(3, 0, -1):
            column = int(input("Please enter right column, you have %s chance(s): " % i))
            if (column <= l):
                break    
    if ((column > l) or (row > h)):
        print("You hava enter wrong matrix row or column")
        return
    sum = 0
    for j in range(0, h):
        sum += matrix[row][j]
    for i in range(0, l):
        sum += matrix[i][column]
    print('The sum of M_tanspose %dth column and %dth row = ' % (column, row), sum)
    # while(True): 

print('M element sum = ', getSumOfTheMatrix(M))
print('M_transpose element sum = ', getSumOfTheMatrix(M_transpose))
countSumOfTheMatrixSSpecialRowAndColumn(M_transpose, 50, 150)