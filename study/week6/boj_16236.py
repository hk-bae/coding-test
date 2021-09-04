import sys
from collections import deque

input = sys.stdin.readline


n = int(input())

graph = [[0] * n for _ in range(n)]
for i in range(n) :
    data = list(map(int,input().split()))
    for j in range(n) :
        graph[i][j] = data[j]
        if data[j] == 9 :
            start_x,start_y = i,j

size = 2 # 아기상어 크기
eat = 0 # 먹은 물고기
total_time = 0 # 시간
distance = 0 # 거리

# 상 좌 우 하
dx = [-1,0,0,1]
dy = [0,-1,1,0]

visited = [[False] * n for _ in range(n)]

# bfs
q = deque([(start_x,start_y,0)]) # 좌표, 현 위치까지의 시간
tmp = []
graph[start_x][start_y] = 0
visited[start_x][start_y] = True


while q :
    now_x,now_y,time = q.popleft()

    # 다음 위치 이동 가능 여부 파악
    for i in range(4) : 
        nx = now_x + dx[i]
        ny = now_y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] :
            # 해당 위치의 물고기 크기가 상어보다 크다면 이동 불가
            if graph[nx][ny] > size : 
                continue
            # 이동 가능    
            else :
                visited[nx][ny] = True
                # 다음 단계에 대해 상,좌,우,하 순으로 들어갈 수 있도록 미리 저장해둔다.
                tmp.append((nx,ny,time+1))

    # 큐가 비었을 경우 다음 거리 단계의 값들을 정렬 후 넣는다.
    if len(q) == 0 :
        tmp.sort() # 상,좌,우,하 순으로 정렬
        find = False
        
        # 이번 단계에서 먹을 물고기가 있는지 확인
        for x,y,t in tmp :
         # 해당 위치 물고기 크기가 상어보다 작다면 먹고 큐,visitied를 초기화
            if 0 < graph[x][y] < size :
                find = True
                # 현재 위치까지의 시간을 더해준다
                total_time += t  
                graph[x][y] = 0 
                eat += 1
                if eat == size : # 상어 크기만큼 먹게 되면 상어크기 1 증가
                    size += 1 
                    eat = 0
                #큐, visited를 초기화하고 현재 위치에서 부터 탐색 다시 시작
                visited = [[False] * n for _ in range(n)]
                visited[x][y] = True
                q = deque([(x,y,0)])
                tmp = []

                break
        
        # 먹을 물고기를 찾지 못했다면 다음 단계 탐색
        if not find :
            # 다음 단계 탐색을 위해 큐에 삽입
            for x,y,t in tmp :
                q.append((x,y,t))
                tmp = []
        
print(total_time)
                
            
