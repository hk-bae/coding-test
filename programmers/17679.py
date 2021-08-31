def solution(m, n, board):
    removed = 0
    
    board = [ list(board[i]) for i in range(m)]
    
    while True :
        removed_set = set()
        removed_now = 0
        for i in range(0,m-1) :
            for j in range(0,n-1) : 
                if board[i][j] != '0' and board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j] and board[i][j] == board[i+1][j+1] :
                    removed_set.update([(i,j),(i,j+1),(i+1,j),(i+1,j+1)])

        for x,y in removed_set :
            removed_now += 1 
            board[x][y] = '0' # 제거 표시
        
        if removed_now == 0 :
            break
        else :
            removed += removed_now
            
        new_board = [['0' for _ in range(n)] for _ in range(m)] # m x n
        
        for j in range(0,n) :
            next = m-1
            for i in range(m-1,-1,-1) :
                if board[i][j] != '0' :
                    new_board[next][j] = board[i][j]
                    next -= 1
                
            if next >= 0 :
                for i in range(next,-1,-1) :
                    new_board[next][j] = '0'
                    
        for i in range(m) :
            for j in range(n) :
                board[i][j] = new_board[i][j]
                    
        
                
    return removed

solution(4,5,	["CCBDE", "AAADE", "AAABF", "CCBBF"])