def rotate_90(key,m) :
    new_key = [[0 for _ in range(m)] for _ in range(m)]
    
    for i in range(m) :
        for j in range(m) :
            new_key[j][m-1-i] = key[i][j]
    
    return new_key

def solution(key, lock):
    
    n = len(lock)
    m = len(key)
    
    board = [[0 for _ in range(n+2*m-2)] for _ in range(n+2*m-2)]
    
    # 가운데 자물쇠 값 넣기
    for i in range(m-1,m-1+n) :
        for j in range(m-1,m-1+n) :
            board[i][j] = lock[i-m+1][j-m+1]
    
    for _ in range(4) : # 회전 4방향에 대해 모두 수행
        key = rotate_90(key,m)

        # 모든 위치 탐색
        for i in range(n+m-1) :
            for j in range(n+m-1) :
                success = True
                
                # key 꼽기
                for k in range(m) :
                    for l in range(m) :
                        board[i+k][j+l] += key[k][l]
                    
        
                # 가운데 자물쇠 값 확인
                for x in range(m-1,m-1+n) :
                    for y in range(m-1,m-1+n) :
                        
                        if board[x][y] != 1  :
                            success = False
                            break
                    
                    if not success : break
        
                                
                if success : break
                    
                # key 빼기
                for k in range(m) :
                    for l in range(m) :
                        board[i+k][j+l] -= key[k][l]
                        
            if success : break
                
        if success: break
        
        
    
    
    return success