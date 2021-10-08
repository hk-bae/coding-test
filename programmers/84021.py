from collections import deque

def compare(list1,list2) :
    for i in range(6):
        for j in range(6):
            if list1[i][j] != list2[i][j] :
                return False
    return True

# 좌표리스트를 (0,0)이 기준인 6x6 행렬 기준으로 변환
def standard(loc_list) :
    # 현재 블럭의 최소 x,y 계산
    min_x = 1e9
    min_y = 1e9
    new_list = [[0 for _ in range(6)] for _ in range(6)]
    
    for x,y in loc_list :
        min_y = min(min_y,y)
        min_x = min(min_x,x)
        
    for x,y in loc_list :
        new_list[x-min_x][y-min_y] = 1
        
    return new_list 

def rotate(loc_array) :
    
    
    tmp = []
    for i in range(6):
        for j in range(6):
            if loc_array[i][j] == 1 :
                tmp.append((j,6-i-1))
    
    return standard(tmp)

# 빈칸 set 반환
def get_loc_list(graph,isPuzzle) :
    block = 1 # 벽
    if isPuzzle :
        block = 0 # 퍼즐이 없는 부분 
        
    n = len(graph)
    visited = [[False for _ in range(n)] for _ in range(n)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    new_list = [] # 빈칸 리스트 또는 퍼즐 리스트 
    index = 0
    for i in range(n):
        for j in range(n) :
            if graph[i][j] != block and not visited[i][j] :
                # ========bfs========
                q = deque([(i,j)])
                visited[i][j] = True
                tmp = []
                
                while q :
                    x,y = q.popleft()
                    tmp.append((x,y))
                    for d in range(4):
                        nx = x+dx[d]
                        ny = y+dy[d]
                        
                        if 0<=nx<n and 0<=ny<n and not visited[nx][ny] :
                            visited[nx][ny] = True
                            if graph[nx][ny] == block :
                                continue
                            q.append((nx,ny))
                
                new_list.append(tmp)
                
    return new_list              
                 
    

def solution(game_board, table):
    answer = 0
    blank_list = get_loc_list(game_board,False)
    puzzle_list = get_loc_list(table,True)
    p_n = len(puzzle_list)
    
    used = [False] * p_n
    # print(blank_list)
    # print(puzzle_list)
    # 모든 빈칸에 대하여 확인
    for blank in blank_list :
        for i,puzzle in enumerate(puzzle_list) :
            flag = False
            if not used[i] :
                puzzle_standard = standard(puzzle)
                
                for _ in range(4) :
                    puzzle_standard = rotate(puzzle_standard)
                    if compare(standard(blank),puzzle_standard) :
                        flag = True
                        used[i] = True
                        break
            if flag :
                answer += len(puzzle)
                break
                
    
    return answer