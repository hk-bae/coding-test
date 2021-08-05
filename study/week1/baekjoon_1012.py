# https://www.acmicpc.net/problem/1012
# bfs
import sys
from collections import deque

input = sys.stdin.readline

def bfs(i,j) :
    visited[i][j] = True
    q = deque([(i,j)])
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<= nx < n and 0 <= ny < m :
                if not visited[nx][ny] and graph[nx][ny] == 1 :
                    q.append((nx,ny))
                    visited[nx][ny] = True
    

t = int(input())

for _ in range(t) :
    n,m,k = map(int,input().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    result = 0
    
    for _ in range(k) :
        x,y = map(int,input().split())
        graph[x][y] = 1

    for i in range(n) :
        for j in range(m) :
           if not visited[i][j] and graph[i][j] == 1 :
            bfs(i,j)
            result += 1
            
    print(result)