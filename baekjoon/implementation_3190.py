import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[0] * (n+2) for _ in range(n+2)]

# 벽 세우기
for i in range(n+2) :
    graph[i][0] = -1
    graph[0][i] = -1
    graph[n+1][i] = -1
    graph[i][n+1] = -1
    
k = int(input())

for _ in range(k) :
    a,b = map(int,input().split())
    graph[a][b] = 1 # 사과
    
turn = deque()

for _ in range(int(input())) :
    x,c = input().split()
    turn.append((int(x),c))
    
nx,ny = 1,1 # 머리 위치
snail = deque([(nx,ny)])

d = 0 # 방향
length = 0 #길이
time = 0

# 오른쪽 아래 왼쪽 위 순서
dx = [0,1,0,-1]
dy = [1,0,-1,0]

while True :
    if turn and time == turn[0][0] :
        _,c = turn.popleft()
        if c == 'L' :
            d = d - 1 if d - 1 >= 0 else 3
        else :
            d = d + 1 if d + 1 < 4 else 0
    
    time += 1
    
    nx += dx[d]
    ny += dy[d]
    
    # 벽을 만난경우(-1) / 자기 몸을 만난 경우(2) / 사과를 만난 경우(1) / 아무 것도 없는 길인 경우 (0)
    
    # 사과를 만난 경우
    if graph[nx][ny] == 1 :
        graph[nx][ny] = 2
        snail.append((nx,ny))
    # 빈 공간인 경우
    elif graph[nx][ny] == 0 :
        graph[nx][ny] = 2
        snail.append((nx,ny))
        tail_x,tail_y = snail.popleft()
        graph[tail_x][tail_y] = 0
    # 자기 몸을 만나거나 벽을 만난 경우
    else :
        print(time)
        break
