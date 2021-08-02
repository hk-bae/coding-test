from collections import deque

max_value = 0

def bfs(x,y) :
    global max_value,n,m
    
    visited[x][y] = True
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    queue = deque([(x,y)])
    size = 1
    
    while queue :
        now_x,now_y = queue.popleft()
        for i in range(4) :
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            
            if 1<=nx<=n and 1<=ny<=m and not visited[nx][ny] and graph[nx][ny] == 1 :
                size += 1
                queue.append((nx,ny))
                visited[nx][ny] = True
                
    max_value = max(max_value,size)
                    

n,m,k = map(int,input().split())

graph = [[0] * (m+1) for _ in range(n+1)]
visited = [[False] * (m+1) for _ in range(n+1)]

for _ in range(k) :
    a,b = map(int,input().split())
    graph[a][b] = 1

for i in range(1,n+1) :
    for j in range(1,m+1) :
        if graph[i][j] == 1 and not visited[i][j] :
            bfs(i,j)
            
print(max_value)