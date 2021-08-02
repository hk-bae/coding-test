import sys

input = sys.stdin.readline

n,m,x,y,k = map(int,input().split())

graph = [[] for _ in range(n)]

for i in range(n) :
    graph[i] = list(map(int,input().split()))
    
command = list(map(int,input().split()))

# 동 1, 서2, 북3, 남4
dx = [0,0,-1,1]
dy = [1,-1,0,0]

dice = [0] * 7

for index in range(k) :
    i = command[index] - 1
    # 이동 불가 범위
    if x + dx[i] < 0 or x + dx[i] >= n or y + dy[i] < 0 or y + dy[i] >= m :
        continue

    # 주사위 위치 이동
    x += dx[i]
    y += dy[i]
    
    # 주사위 면 이동
    if i == 0 : # 동
        dice[1],dice[3],dice[6],dice[4] = dice[4],dice[1],dice[3],dice[6]
    elif i == 1 : # 서
        dice[1],dice[3],dice[6],dice[4] = dice[3],dice[6],dice[4],dice[1]
    elif i == 2 : # 북
        dice[1],dice[5],dice[6],dice[2] = dice[5],dice[6],dice[2],dice[1]
    else : # 남
        dice[1],dice[5],dice[6],dice[2] = dice[2],dice[1],dice[5],dice[6]
        
    print(dice[1]) # 상단에 쓰여진 값 출력
    
    if graph[x][y] == 0 : # 이동한 칸에 쓰여진 수가 0인 경우
        graph[x][y] = dice[6]  # 바닥면에 쓰여진 수 복사
    else :
        dice[6] = graph[x][y]
        graph[x][y] = 0
    
    