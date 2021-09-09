import sys

input = sys.stdin.readline

# 상어위치, 먹은 물고기 수 전달
def backtracking(x,y,value,graph,fish_info) :
    global result
    # 그래프 복사
    new_graph = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4) :
        for j in range(4) :
            new_graph[i][j] = graph[i][j]

    new_fish_info = dict()
    
    # 딕셔너리 복사
    for k in fish_info.keys() :
        new_fish_info[k] = [0,0,0]
        new_fish_info[k][0] = fish_info[k][0]
        new_fish_info[k][1] = fish_info[k][1]
        new_fish_info[k][2] = fish_info[k][2]

    # 물고기 이동
    for num in range(1,17) :
        if not remain[num] : # 먹힌 물고기
            continue
        
        fish_x,fish_y,d = new_fish_info[num] # num번째 물고기 위치, 방향
        
        d -= 1
        
        # 이동 가능할 때까지 회전
        for _ in range(8) :
            d += 1
            if d > 8 : d = 1
                
            nx = fish_x + dx[d]
            ny = fish_y + dy[d]
            # 범위내이고 상어가 아니면 자리 교체
            if 0<=nx<4 and 0<=ny<4 and graph[nx][ny] != -1: 
                num2 = new_graph[nx][ny] # 교체되는 물고기 번호 또는 빈공간
                new_graph[nx][ny],new_graph[fish_x][fish_y] = new_graph[fish_x][fish_y],new_graph[nx][ny]     
                new_fish_info[num] = [nx,ny,d]
                if num2 != 0 :
                    new_fish_info[num2][0] = fish_x
                    new_fish_info[num2][1] = fish_y
                break
        

    # 상어 : 더 먹을 물고기가 있는지 탐색
    _,_,d = fish_info[-1] # 상어의 이동 방향
    
    eat = False
    now_x,now_y = x,y
    while True :
        nx = now_x + dx[d]
        ny = now_y + dy[d]
        
        if 0<=nx<4 and 0<=ny<4 :
            if new_graph[nx][ny] != 0: # 먹을 물고기가 있는 경우
                num = new_graph[nx][ny] # 물고기 번호
                new_graph[nx][ny] = -1 # 상어 이동
                new_graph[x][y] = 0
                new_fish_info[-1][2] = new_fish_info[num][2]
                remain[num] = False 
                backtracking(nx,ny,value+num,new_graph,new_fish_info)
                new_graph[nx][ny] = num
                new_graph[x][y] = -1
                new_fish_info[-1][2] = d
                remain[num] = True
                eat = True
            now_x = nx
            now_y = ny               
        else : # 경계 밖인 경우
            break

    # 더 먹을 물고기가 없다면            
    if not eat :
        result = max(result,value)
        return
    

    
    
dx = [0,-1,-1,0,1,1,1,0,-1]
dy = [0,0,-1,-1,-1,0,1,1,1]

graph = [[] for _ in range(4)]
remain = [True] * 17 # 살아남은 물고기

fish_info = dict()

for i in range(4) :
    data = list(map(int,input().split()))
    for j in range(0,8,2) :
        graph[i].append(data[j]) # 물고기 번호
        fish_info[data[j]] = [i,j//2,data[j+1]] # 물고기 위치, 방향 저장 


num = graph[0][0] 
d = fish_info[num][2]
fish_info[-1] = [0,0,d]
remain[num] = False
graph[0][0] = -1 # 상어 표시
result = num

backtracking(0,0,num,graph,fish_info)

print(result)