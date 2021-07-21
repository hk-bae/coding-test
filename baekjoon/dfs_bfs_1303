from collections import deque

def bfs(x,y) :
    global n,m
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    queue = deque([(x,y)])
    visited[x][y] = True
    
    k = graph[x][y]
    
    cnt = 1
    
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == k :
                visited[nx][ny] = True
                queue.append((nx,ny))
                cnt += 1

    if k == 'W' :
        w_list.append(cnt)
    else :
        b_list.append(cnt)
    

m,n = map(int,input().split())
graph = []
visited = [[False] * m for _ in range(n)]

w_list = []
b_list = []

w_power = 0
b_power = 0

for i in range(n) :
    graph.append(list(input()))
    
for i in range(n) :
    for j in range(m) :
         if not visited[i][j] :
                bfs(i,j)

for pw in w_list :
    w_power += pow(pw,2)
    
for pw in b_list :
    b_power += pow(pw,2)
    
print(w_power,b_power)