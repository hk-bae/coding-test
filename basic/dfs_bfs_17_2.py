from collections import deque

n,k = map(int,input().split())

graph = []
virus = []

for i in range(n) :
    graph.append(list(map(int,input().split())))
    for j in range(n) :
        if graph[i][j] != 0 :
            #graph[i][j]의 바이러스가 (i,j)에 있다.
            virus.append((graph[i][j],i,j))
            
virus.sort() # 바이러스 번호가 낮은 순으로 정렬

s,target_x,target_y = map(int,input().split())

queue = deque(virus)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# s초 반복
while s > 0 :
    s -= 1
    length = len(queue)
    # 큐에 들어있는 바이러스 수 만큼 반복
    for _ in range(length) :
        v,x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0 :
                graph[nx][ny] = v
                queue.append((v,nx,ny))
                
print(graph[target_x-1][target_y-1])
