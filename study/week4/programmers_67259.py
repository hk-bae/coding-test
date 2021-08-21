# https://programmers.co.kr/learn/courses/30/lessons/67259

import heapq

def solution(board):
    answer = 0

    # 상하좌우
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    n = len(board)
    distance = [[1e9] * n for _ in range(n)]
    q = []
    heapq.heappush(q,(-500,0,0,-1)) # dist,x,y,d
    distance[0][0] = -500

    while q :
        dist,now_x,now_y,d = heapq.heappop(q)
        
        if distance[now_x][now_y] + 500 < dist :
            continue

        for i in range(4) :
            nx = now_x + dx[i]
            ny = now_y + dy[i]


            if 0<=nx<n and 0<=ny<n and board[nx][ny] != 1 : 
                if d == i : # 같은 방향
                    cost = dist + 100 # 직선도로
                else :
                    cost = dist + 600 # 코너 + 직선도로
                
                if cost < distance[nx][ny] :
                        distance[nx][ny] = cost
                        heapq.heappush(q,(cost,nx,ny,i))
                elif cost < distance[nx][ny] + 500 :
                    heapq.heappush(q,(cost,nx,ny,i))
                    
                    
    answer = distance[n-1][n-1]    

    return answer