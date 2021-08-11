import sys
from collections import deque
from itertools import combinations
import copy

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[0 for _ in range(n)] for _ in range(n)]
virus = [] # 바이러스 위치
empty = 0 # 빈공간 개수

for i in range(n) :
    data = list(map(int,input().split()))
    for j in range(n) :
        graph[i][j] = data[j]
        if data[j] == 2 :
            virus.append((i,j))
        elif data[j] == 0 :
            empty += 1 # 빈공간 카운트

# m개의 활성화될 바이러스 후보군
candidate = combinations(virus,m)

res = 1e9

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 모든 후보군에 대해 활성화시켜보고 bfs로 테스트
for c in candidate :
    test = copy.deepcopy(graph)
    test_empty = empty # 테스트 후 빈공간 확인을 위해 저장
    test_time = 0
    q = deque()
    visited = [[False] * n for _ in range(n)] 
    
    for x,y in c :
        test[x][y] = 3 # 바이러스 활성화
        q.append((x,y,0))
        visited[x][y] = True
    
    # bfs 
    while q : 
        x,y,time = q.popleft()
        if test_empty == 0 : # 빈공간이 없는 경우 종료
            break
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            # 방문안한 곳 중 벽이 아닌 곳에 대해서
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and test[nx][ny] != 1 :
                visited[nx][ny] = True
                if test[nx][ny] == 0 : # 빈 공간인 경우
                    test_empty -= 1
                # 빈공간 또는 비활성 바이러스에 대하여 전이시킨다.
                test[nx][ny] = 3
                q.append((nx,ny,time+1))
                test_time = max(time+1,test_time)
                
    # 모두 전염시킨 경우에 한해서
    if test_empty == 0 : 
        res = min(test_time,res)


if res == 1e9 :
    print(-1)
else :
    print(res)

                     

    
    

    