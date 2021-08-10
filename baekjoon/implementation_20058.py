import sys
from collections import deque

# 2^l x 2^l 크기를 모두 회전한 배열 돌려준다.
def rotate_clock(l) :
    global n,graph

    size = pow(2,l) # 격자 크기

    result = [[0 for _ in range(n)] for _ in range(n)]
    # 2^l x 2^l 으로 나눠야함
    for i in range(0,n,size) :
        for j in range(0,n,size):
            # 각 격자에 대하여 회전
            for s in range(0,size) :
                for t in range(0,size) :
                    result[i+t][j+size-s-1] = graph[i+s][j+t]
    # 복사
    for i in range(n) :
        for j in range(n):
            graph[i][j] = result[i][j]
            
unit_n,q = map(int,input().split())
n = pow(2,unit_n)
graph = [list(map(int,input().split())) for _ in range(n)]

data = list(map(int,input().split()))

# bfs 탐색을 위한 방문 배열
visited = [ [False] * n for _ in range(n)]

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# q회 반복
for l in range(q) :
    # 단게 L 회전
    if data[l] != 0 :
        rotate_clock(data[l])
    
    melt_ice = []
     # 모든 칸에 대해 상하좌우 확인
    for x in range(n) :
        for y in range(n) :
            if graph[x][y] <= 0 : # 얼음이 있는 경우만 체크
                continue
            cnt = 0
            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<n and graph[nx][ny] > 0 : # 범위내에 있고 얼음이 존재한다면
                    cnt +=1
            if cnt < 3 : # 3개 미만 인접한 경우
                melt_ice.append((x,y))

    for x,y in melt_ice :
        graph[x][y] -= 1            
    
remain = 0 # 남은 얼음
cnt = 0 # 덩어리 크기

for x in range(n) :
    for y in range(n) :
        remain += graph[x][y] # 남아있는 얼음의 합
        if graph[x][y] > 0 and not visited[x][y]: # 얼음이 존재하는 방문 안한 구간에 대해 bfs xkator
            q = deque([(x,y)])
            visited[x][y] = True
            tmp_cnt = 1
            while q :
                now_x,now_y = q.popleft()
                for i in range(4) :
                    nx = now_x + dx[i]
                    ny = now_y + dy[i]
                    if 0<=nx<n and 0<=ny<n and graph[nx][ny] > 0 and not visited[nx][ny] :
                        visited[nx][ny] = True
                        q.append((nx,ny))
                        tmp_cnt += 1
                            
            cnt = max(cnt,tmp_cnt) # 가장 큰 덩어리가 차지하는 칸의 개수

if cnt == 1 : # 덩어리는 두 칸 이상
    cnt = 0
    
print(remain)
print(cnt)