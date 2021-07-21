from collections import deque

def bfs(x,y,i) :
    global n,m
    
    queue = deque([(x,y,i)])
    visited[x][y] = True

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
        
    while queue :
        now = queue.popleft()
      
        if now[0] == n-1 and now[1] == m-1 :
            return now[2]
        
        for i in range(4) :
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1 :
                queue.append((nx,ny,now[2] + 1))
                visited[nx][ny] = True
                
        
n,m = map(int,input().split())

graph = []
visited = [[False] * m for _ in range(n)]

graph = [[int(i) for i in list(input())] for _ in range(n)]

print(bfs(0,0,1))