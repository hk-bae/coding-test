import sys
import copy
from collections import deque

input = sys.stdin.readline

# 이전에 설치한 벽의 시작 위치, 현재까지 안전영역 cnt, 벽의 개수 k
def dfs(start,k) :
    global n,m,safe_area
    # 벽 3개 설치 이전
    if k < 3 :
        for i in range(start, n*m) :
            x = i // m
            y = i % m
            if graph[x][y] == 0 :
                graph[x][y] = 1
                dfs(i+1,k+1)
                graph[x][y] = 0
    else :
        cnt = spread_and_count(copy.deepcopy(graph)) # 바이러스 전파 후 안전 영역 개수 확인
        safe_area = max(safe_area,cnt)   
        
def spread_and_count(data) :
    global n,m
    cnt = 0

    q = deque(virus)

    while q :
        x,y = q.popleft()
        # 모든 방향에 대해서
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and data[nx][ny] == 0:
                q.append((nx,ny))
                data[nx][ny] = 2
    

    # 바이러스 개수 확인
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0 :
                cnt += 1

    return cnt
                
            
    
n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

virus = [] # 바이러스 위치
dx = [-1,1,0,0]
dy = [0,0,-1,1]

safe_area = 0 # 안전영역 개수

for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 2 :
            virus.append((i,j))


dfs(0,0)
print(safe_area)