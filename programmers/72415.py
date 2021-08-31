from itertools import permutations
from collections import deque


# 시작점에서 도착점까지의 조작 횟수 ( 엔터 제외 )
def get_distance(s_x,s_y,e_x,e_y) :
    global my_board
    q = deque([(s_x,s_y,0)])
    visited = [[-1] * 4 for _ in range(4)]
    visited[s_x][s_y] = 0
    
    # 상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while q :
        now_x,now_y,dist = q.popleft()
        if now_x == e_x and now_y == e_y :
            break
        
        for i in range(4) :
            # 한칸 이동
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0<=nx<4 and 0<=ny<4 and visited[nx][ny] == -1 : 
                visited[nx][ny] = dist + 1
                q.append((nx,ny,dist+1))
            
            # ctrl 이동
            if i == 0 : # 상
                for j in range(now_x-1,-1,-1) : 
                    if my_board[j][now_y] != 0 or j == 0:
                        if visited[j][now_y] == -1 :
                            visited[j][now_y] = dist + 1
                            q.append((j,now_y,dist+1))
                        break
                
            elif i == 1 : # 하
                for j in range(now_x+1,4) :
                    if my_board[j][now_y] != 0 or j == 3:
                        if visited[j][now_y] == -1 :
                            visited[j][now_y] = dist + 1
                            q.append((j,now_y,dist+1))
                        break
            elif i == 2 : # 좌
                for j in range(now_y-1,-1,-1) :
                    if my_board[now_x][j] != 0 or  j == 0 :
                        if visited[now_x][j] == -1 :
                            visited[now_x][j] = dist + 1
                            q.append((now_x,j,dist+1))
                        break
            else : # 우
                for j in range(now_y+1,4) :
                    if my_board[now_x][j] != 0 or j == 3:
                        if visited[now_x][j] == -1 :
                            visited[now_x][j] = dist + 1
                            q.append((now_x,j,dist+1))
                        break
                    

        
    return visited[e_x][e_y]

# i번쟤 순서에 x,y에서 출발, cnt는 현재 조작 횟수
def backtracking(orders,i,x,y,cnt) :
    global n,answer,pairs,my_board
    
    if cnt >= answer :
        return
    
    if i == n : 
        answer = min(answer,cnt) # 최소값 갱신
        return

    for a in range(4) :
        for b in range(4) :
            print(my_board[a][b],end = ' ')
        print()
    print("----")
    
    now = orders[i]
    p0_x,p0_y = pairs[now][0]
    p1_x,p1_y = pairs[now][1]
    
    # p0 먼저
    new_cnt = cnt + get_distance(x,y,p0_x,p0_y)
    new_cnt += get_distance(p0_x,p0_y,p1_x,p1_y) + 2 # 각 쌍간의 이동 + 엔터 2회
    print(p0_x,p0_y,p1_x,p1_y)
    my_board[p0_x][p0_y] = 0
    my_board[p1_x][p1_y] = 0
    backtracking(orders,i+1,p1_x,p1_y,new_cnt)
    my_board[p0_x][p0_y] = now
    my_board[p1_x][p1_y] = now
    
    # p1 먼저
    new_cnt = cnt + get_distance(x,y,p1_x,p1_y) 
    new_cnt += get_distance(p1_x,p1_y,p0_x,p0_y) + 2 # 각 쌍간의 이동 + 엔터 2회

    
    my_board[p0_x][p0_y] = 0
    my_board[p1_x][p1_y] = 0
    backtracking(orders,i+1,p0_x,p0_y,new_cnt)
    my_board[p0_x][p0_y] = now
    my_board[p1_x][p1_y] = now
    

    

def solution(board, r, c):
    global n,answer,pairs,my_board
    
    answer = 1e9
    remain_num = [False] * 7  # 보드에 남은 카드 
    pairs = [[] for _ in range(7)] # 카드 쌍의 위치
    
    my_board = [[0] * 4 for _ in range(4)]

    for i in range(4) :
        for j in range(4) :
            if board[i][j] != 0 :
                remain_num[board[i][j]] = True
                pairs[board[i][j]].append((i,j))
            my_board[i][j] = board[i][j]

    data = []
    n = 0
    # 남은 카드 번호 저장
    for i in range(1,7) :
        if remain_num[i] :
            data.append(i)
            n += 1
    

    # 남은 카드에 대해 찾을 순서를 정함
    candidates = list(permutations(data,n))
    for orders in candidates : 
        backtracking(orders,0,r,c,0)
        
    
    return answer

board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]	 
r,c = 1,0

print(solution(board,r,c))