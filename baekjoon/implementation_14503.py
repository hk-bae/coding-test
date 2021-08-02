import sys
input = sys.stdin.readline

n,m = map(int,input().split())
x,y,d = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]
# 0 : 상, 1 : 우, 2 : 하, 3 : 좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]

graph[x][y] = 2 # 청소 표시
result = 1
cnt = 0 # 확인 방향 개수

    
while True :

    i = d-1 if d-1 >= 0 else 3 # 현재 위치의 왼쪽 방향
    nx = x + dx[i] 
    ny = y + dy[i]
    # 네 방향 모두 확인한 경우
    if cnt == 4 :
        j = (d + 2) % 4 # 현재 방향의 후진 방향
        nx = x + dx[j]
        ny = y + dy[j]
        
        # 후진 방향이 벽인 경우 종료
        if nx < 0 or nx >= n or ny <0 or ny >= m or graph[nx][ny] == 1 :
            break
        else : # 현재 방향을 유지한 채 후진
            x = nx
            y = ny
            cnt = 0
    # 청소할 공간이 없는 경우
    elif nx not in range(0,n) or ny not in range(0,m) or graph[nx][ny] == 1 or graph[nx][ny] == 2 : 
        d = i # 회전만
        cnt += 1
    # 현재 방향의 왼쪽 위치에 청소가 가능한 경우
    elif graph[nx][ny] == 0 : 
        d = i
        x = nx # 회전 후 이동
        y = ny # 회전 후 이동
        graph[x][y] = 2
        result += 1
        cnt = 0

print(result)
