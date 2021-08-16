import sys
from collections import deque

input = sys.stdin.readline

n,m,t = map(int,input().split())

graph = [deque(list(map(int,input().split()))) for _ in range(n)] # n개의 원판

dx = [1,-1,0,0]
dy = [0,0,-1,1]

sum_value = 0
total_num = n*m


for i in range(n) :
    for j in range(m) : 
        sum_value += graph[i][j]


        
command = []
for _ in range(t) :
    x,d,k = map(int,input().split())
    if d == 1 :
        k = -k # 반시계 방향으로 변환
    command.append((x,k))

for x,k in command :
    # 1. 회전
    for i in range(n) : 
        if (i+1) % x == 0 : # x 배수인 경우
            graph[i].rotate(k) # k방향 회전

    # print("## after rotate",x,k)
    # for i in range(n) :
    #     for j in range(m) :
    #         print(graph[i][j],end= ' ')
    #     print()
    # 2. 인접하면서 같은 수 제거
    erase = False # 하나라도 지워진 것이 있는지 체크
    visited = [[False] * m for _ in range(n)]

    for i in range(n) :
        for j in range(m) :
            # 이미 방문한 곳이라면 패스
            if visited[i][j] or graph[i][j] == 0 : 
                continue
            
            visited[i][j] = True
            value = graph[i][j] # 현재 값 저장
            value_erased = False # 현재 값이 지워졌는지 체크
            q = deque([(i,j)])
            
            while q : # bfs 
                now_x,now_y = q.popleft()
                for d in range(4) :
                    nx = now_x + dx[d]
                    ny = (now_y + dy[d]) % m

                    if 0<=nx<n and not visited[nx][ny] :
                        if graph[nx][ny] == value : # 인접한 값이 동일한 값이라면 제거
                            visited[nx][ny] = True
                            graph[nx][ny] = 0
                            value_erased = True
                            q.append((nx,ny))

                            total_num -= 1
                            sum_value -= value

            if value_erased : # 지워진 값이 존재 한다면
                graph[i][j] = 0
                erase = True
                total_num -= 1
                sum_value -= value
    if total_num == 0 :
        break
    
    if not erase : # 지워진 값이 없는 경우            
        avg = sum_value / total_num # 평균 값
        for i in range(n) :
            for j in range(m) :
                if graph[i][j] == 0 :
                    continue
                
                if graph[i][j] > avg :
                    graph[i][j] -= 1
                    sum_value -= 1
                elif graph[i][j] < avg :
                    graph[i][j] += 1
                    sum_value += 1

    # print("##after erase",x,k)
    # for i in range(n) :
    #     for j in range(m) :
    #         print(graph[i][j],end= ' ')
    #     print()

print(sum_value)

    





