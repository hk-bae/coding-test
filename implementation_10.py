# Q10. 자물쇠와 열쇠 - 이것이 취업을 위한 코딩테스트다 518pg
# 2020 카카오 신입 공채 문제
# https://prgorammers.co.kr/learn/courses/30/lessons/60059

def solution(key, lock):
    n = len(lock)
    m = len(key)
    extended_lock = [[0] * (3 * n) for _ in range((3*n))]
    
    for i in range(n,2*n) :
        for j in range(n,2*n) :
            extended_lock[i][j] = lock[i-n][j-n]
    
    
    try_unlock = [[0] * (3*n) for _ in range(3*n)]
    
    for _ in range(0,4) :
        key = rotate_90_degree(key)
        for x in range(n*2) :
            for y in range(n*2) :
                for i in range(m) :
                    for j in range(m) :
                        extended_lock[x+i][y+j] += key[i][j]
                if check_unlock(extended_lock,n) == True : return True
                
                for i in range(m) :
                    for j in range(m) :
                        extended_lock[x+i][y+j] -= key[i][j]
        
    return False


def check_unlock(matrix,n):
    for i in range(n,2*n) :
        for j in range(n,2*n):
            if matrix[i][j] == 0 or matrix[i][j] == 2 : return False
    return True

def rotate_90_degree(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n) :
        for j in range(m):
            result[j][n-i-1] =matrix[i][j]
    return result
