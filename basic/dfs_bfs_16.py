#https://www.acmicpc.net/problem/14502

# dfs
from itertools import combinations

n,m = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))
    
space = [] # 벽을 세울 수 있는 공간
virus = [] # 바이러스 위치
for i in range(n):
    for j in range(m) :
        if graph[i][j] == 0 :
            space.append((i,j))
        elif graph[i][j] == 2 :
            virus.append((i,j))


tmp = [[0] * m for _ in range(n) ]

# 각 바이러스(x,y)에 대하여 dfs를 통해 전이
def dfs(x,y) :
    # 상,하,좌,우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
   
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny <0 or ny >= m :
          continue
        else :
          if tmp[nx][ny] == 0 :
            tmp[nx][ny] = 2
            dfs(nx,ny)
            
#안전 영역 구하기
def getSafeArea() :
    count = 0
    for i in range(len(tmp)) :
        for j in range(len(tmp[i])) :
            if tmp[i][j] == 0 : count += 1
    return count
    
    
candidates = list(combinations(space,3)) # 벽을 놓을 수 있는 가능한 모든 3개 조합

maxSafeArea = -1

for candidate in candidates :
    # tmp 초기화 
    for i in range(n) : 
        for j in range(m) :
            tmp[i][j] = graph[i][j]  

    # 가능한 조합들에 대하여 벽 세우기
    for i,j in candidate :
        tmp[i][j] = 1
    
    #각 바이러스에 대하여 전이하기
    for x,y in virus :
        dfs(x,y)
    
    maxSafeArea = max(maxSafeArea,getSafeArea())

print(maxSafeArea)

# bfs

