from itertools import combinations
from collections import deque
import copy

n,m = map(int,input().split())

graph = []
empty = [] # 빈공간 위치
virus = [] # 바이러스 위치

empty_num = 0 # 안전 지대 갯수

for i in range(n) :
    graph.append(list(map(int,input().split())))
    for j in range(m) :
        if graph[i][j] == 0 :
            empty.append((i,j))
            empty_num += 1
        elif graph[i][j] == 2 :
            virus.append((i,j))
            
# 빈 공간 중 3개를 뽑는 모든 조합
candidates = list(combinations(empty,3))

result = 0

# 모든 조합에 대해 확인
for a,b,c in candidates :
    
    tmp = copy.deepcopy(graph)

    # 벽 세우기
    tmp[a[0]][a[1]] = 1
    tmp[b[0]][b[1]] = 1
    tmp[c[0]][c[1]] = 1
    
    queue = deque(virus)

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    # 현재 빈 공간
    tmp_empty = empty_num - 3
    
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                # 빈 공간인 경우 바이러스 전파
                if tmp[nx][ny] == 0 :
                    queue.append((nx,ny))
                    tmp[nx][ny] = 2
                    # 안전지대 하나 감소
                    tmp_empty -= 1
   
    result = max(tmp_empty,result)
                    
print(result)     
