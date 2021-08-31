from collections import deque

def solution(board):
    answer = 0
    n = len(board)
    
    h_visited = dict() # 가로 방향으로 방문 여부 key : (x,y) value : Bool
    v_visited = dict() # 세로 방향
    
    for i in range(n) :
        for j in range(n) :
            h_visited[(i,j)] = False
            v_visited[(i,j)] = False
            
    # 상,하,좌,우 이동
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    h_cost = [[1e9 for _ in range(n)] for _ in range(n)] # 가로 방향 시간 비용 리스트
    v_cost = [[1e9 for _ in range(n)] for _ in range(n)] # 세로 방향 시간 비용 리스트
    
    q = deque([((0,0),0,True)]) # head,cost,isHorizontal
    h_visited[(0,0)] = True
    h_cost[0][0] = 0 
              
    while q :
        loc,cost,isHorizontal = q.popleft()
        now_x,now_y = loc
            
        # 상,하,좌,우 이동
        for d in range(4) : 
            nx = now_x + dx[d]
            ny = now_y + dy[d]
            
            if 0<=nx<n and 0<=ny<n and board[nx][ny] != 1:
                if isHorizontal : # 가로 방향에서 이동
                    if 0<=ny+1<n and board[nx][ny+1] != 1 : # 꼬리 방향 이동 가능 확인
                        if not h_visited[(nx,ny)] : #  방문여부 확인
                            h_visited[(nx,ny)] = True
                            h_cost[nx][ny] = cost + 1 # 현재 비용 + 1
                            q.append(((nx,ny),cost+1,isHorizontal))
                else : # 세로방향에서 이동
                    if 0<=nx+1<n and board[nx+1][ny] != 1 and not v_visited[(nx,ny)]: # 꼬리 방향 범위 확인 + 방문 여부 확인
                        v_visited[(nx,ny)] = True
                        v_cost[nx][ny] = cost + 1
                        q.append(((nx,ny),cost+1,isHorizontal))
        
        # 4 방향 회전 
        # 기존 가로방향 회전 가능 여부 판단
        if isHorizontal :
            if 0<=now_x + 1<n and 0<=now_y +1<n : # 아래 두 칸이 비어 있는 경우
                if board[now_x+1][now_y+1] != 1 and board[now_x+1][now_y] != 1: # 벽 확인
                    left_nx,left_ny = now_x,now_y 
                    right_nx,right_ny = now_x,now_y+1
                    # 왼쪽
                    if not v_visited[(left_nx,left_ny)] :  #방문여부 확인
                        v_visited[(left_nx,left_ny)] = True
                        v_cost[left_nx][left_ny] = cost + 1
                        q.append(((left_nx,left_ny),cost+1,not isHorizontal)) # 방향 바꿔서 큐에 삽입

                    # 오른쪽
                    if not v_visited[(right_nx,right_ny)] :  # 방문여부 확인
                        v_visited[(right_nx,right_ny)] = True
                        v_cost[right_nx][right_ny] = cost + 1
                        q.append(((right_nx,right_ny),cost+1,not isHorizontal)) # 방향 바꿔서 큐에 삽입
                        
            if 0<=now_x - 1<n and 0<=now_y +1<n : # 위 두 칸이 비어 있는 경우
                if board[now_x-1][now_y+1] != 1 and board[now_x-1][now_y] != 1: # 벽 확인
                    left_nx,left_ny = now_x-1,now_y 
                    right_nx,right_ny = now_x-1,now_y+1
                    # 왼쪽
                    if not v_visited[(left_nx,left_ny)] :  #방문여부 확인
                        v_visited[(left_nx,left_ny)] = True
                        v_cost[left_nx][left_ny] = cost + 1
                        q.append(((left_nx,left_ny),cost+1,not isHorizontal)) # 방향 바꿔서 큐에 삽입

                    # 오른쪽
                    if not v_visited[(right_nx,right_ny)] :  # 방문여부 확인
                        v_visited[(right_nx,right_ny)] = True
                        v_cost[right_nx][right_ny] = cost + 1
                        q.append(((right_nx,right_ny),cost+1,not isHorizontal)) # 방향 바꿔서 큐에 삽입                        

        else : 
            # 기존 세로 방향 회전 가능 여부 판단
            if 0<=now_x +1<n and 0<=now_y+1<n : # 오른쪽이 비어있는 경우
                if board[now_x+1][now_y+1] != 1 and board[now_x][now_y+1] != 1: # 벽 확인
                    bottom_nx,bottom_ny = now_x+1,now_y # 오른쪽 아래
                    top_nx,top_ny = now_x,now_y
                    
                    if not h_visited[(bottom_nx,bottom_ny)] : # 방문여부 확인
                        h_visited[(bottom_nx,bottom_ny)] = True
                        h_cost[bottom_nx][bottom_ny] = cost + 1
                        q.append(((bottom_nx,bottom_ny),cost+1,not isHorizontal)) # 방향 바꿔서 큐에 삽입
                        
                    if not h_visited[(top_nx,top_ny)] : # 방문여부 확인
                        h_visited[(top_nx,top_ny)] = True
                        h_cost[top_nx][top_ny] = cost + 1
                        q.append(((top_nx,top_ny),cost+1,not isHorizontal)) # 방향 바꿔서 큐에 삽입

            if 0<=now_x+1<n and 0<=now_y-1<n : # 왼쪽이 비어있는 경우
                if board[now_x+1][now_y-1] != 1 and board[now_x][now_y-1] != 1: # 벽 확인
                    top_nx,top_ny = now_x,now_y-1
                    bottom_nx,bottom_ny = now_x+1,now_y-1
                    
                    if not h_visited[(top_nx,top_ny)] :
                        h_visited[(top_nx,top_ny)] = True
                        h_cost[top_nx][top_ny] = cost + 1
                        q.append(((top_nx,top_ny),cost+1,not isHorizontal)) # 방향 바꿔서 큐에 삽입
                        
                    if not h_visited[(bottom_nx,bottom_ny)] :
                        h_visited[(bottom_nx,bottom_ny)] = True
                        h_cost[bottom_nx][bottom_ny] = cost + 1
                        q.append(((bottom_nx,bottom_ny),cost+1,not isHorizontal)) # 방향 바꿔서 큐에 삽입
            
    
    answer = min(v_cost[n-2][n-1], h_cost[n-1][n-2])
            
            
    return answer