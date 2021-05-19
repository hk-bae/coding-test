# N x M 행렬을 90도 회전하는 함수

def rotate_90_degree(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n) :
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result
