import sys 

input = sys.stdin.readline

# 현재까지 감시 공간 개수, i번째 cctv
def dfs(cnt,i) :
    global k, count
    if i < k :
        num = cctv[i][0]
    
        length = 0
    
        if num == 2 :
            length = 2
        elif num == 5 :
            length = 1
        else :
            length = 4

        # 90도 회전
        for d in range(length) :
            new_cnt = check(i,d,cnt)
            dfs(new_cnt,i+1)
            uncheck(i)
   
    else :
        # 최댓값 갱신
        count = max(count,cnt)

def monitor(i,x,y,d) :
    global n,m
    cnt = 0
    nx = x + dx[d]
    ny = y + dy[d]
    
    # 범위를 벗어나거나 벽을 만나지 않을 대 까지
    while 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 6:
        if graph[nx][ny] == 0 : 
            cnt += 1
            graph[nx][ny] = 7
            visited[i].append((nx,ny))
        
        nx += dx[d]
        ny += dy[d]
    
    return cnt

            
def check(i,d,cnt) :
    num,x,y = cctv[i]
    new_cnt = cnt
    
    # 1번 cctv 
    if num == 1 :
        new_cnt += monitor(i,x,y,d)
        
    # 2번 cctv
    elif num == 2 :
        if d == 0 : 
            new_cnt += monitor(i,x,y,2) # 좌
            new_cnt += monitor(i,x,y,3) # 우
        else : 
            new_cnt += monitor(i,x,y,0) # 상
            new_cnt += monitor(i,x,y,1) # 하
    
    # 3번 cctv
    elif num == 3 :
        if d == 0 : 
            new_cnt += monitor(i,x,y,0) # 상
            new_cnt += monitor(i,x,y,3) # 우
        elif d == 1 :
            new_cnt += monitor(i,x,y,0) # 상
            new_cnt += monitor(i,x,y,2) # 좌
        elif d == 2 :
            new_cnt += monitor(i,x,y,1) # 하
            new_cnt += monitor(i,x,y,2) # 좌
        else :
            new_cnt += monitor(i,x,y,1) # 하
            new_cnt += monitor(i,x,y,3) # 우
            
    elif num == 4 :
        if d == 0 :
            new_cnt += monitor(i,x,y,0) # 상
            new_cnt += monitor(i,x,y,2) # 좌
            new_cnt += monitor(i,x,y,3) # 우
        elif d == 1:
            new_cnt += monitor(i,x,y,0) # 상
            new_cnt += monitor(i,x,y,2) # 좌
            new_cnt += monitor(i,x,y,1) # 하
        elif d == 2:
            new_cnt += monitor(i,x,y,1) # 하
            new_cnt += monitor(i,x,y,2) # 좌
            new_cnt += monitor(i,x,y,3) # 우
        else :
            new_cnt += monitor(i,x,y,1) # 하
            new_cnt += monitor(i,x,y,3) # 우
            new_cnt += monitor(i,x,y,0) # 상
    else :
        new_cnt += monitor(i,x,y,0) # 상
        new_cnt += monitor(i,x,y,1) # 하
        new_cnt += monitor(i,x,y,2) # 좌
        new_cnt += monitor(i,x,y,3) # 우
    return new_cnt

def uncheck(i) :
    for x,y in visited[i] :
        graph[x][y] = 0

    visited[i] = [] 
            
n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]
cctv = [] # (번호,x,y)
total = 0 # 전체 빈 공간의 갯수
count = 0 # 감시 공간 갯수

# 상 하 좌 우 
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 0 :
            total += 1
        elif graph[i][j] != 6 :
            cctv.append((graph[i][j],i,j))
            
k = len(cctv) # cctv 개수
visited = [[] for _ in range(k)] # i번째 cctv가 추가로 감시하는 좌표의 위치
if k != 0 :
    dfs(0,0)
print(total - count)