import sys

input = sys.stdin.readline

def rotate(d) :
    if d == 0 :
        return 1
    elif d == 1 :
        return 2
    elif d == 2 :
        return 3
    else :
        return 0

graph = [[False] * 101 for _ in range(101)] # 좌표를 찍어주는 그래프

n = int(input())

#우 상 좌 하
dx = [0,-1,0,1]
dy = [1,0,-1,0]

# 각 드래곤 커브 별로 다음 이동 방향을 저장 
dp = [[-1] * 1024 for _ in range(n)]

# i번째 드래곤 커브
for i in range(n) : 
    y,x,d,g = map(int,input().split())
    # 0세대에서의 이동 방향
    dp[i][0] = d 
    # k세대
    for k in range(1,g+1) : # 1,2,...,g 세대
        for t in range(pow(2,k-1)) :
            # 다음 2^k-1 개는 이전 2^k-1 개를 뒤에서부터 하나씩 회전 시킨 방향과 같다
            dp[i][pow(2,k-1) + t] = rotate(dp[i][pow(2,k-1)-t-1])
    
    # 이제 dp를 돌면서 그래프에 점을 찍는다
    graph[x][y] = True
    nx = x 
    ny = y
    for j in range(pow(2,g)) :
        nx += dx[dp[i][j]]
        ny += dy[dp[i][j]]
        graph[nx][ny] = True


result = 0
# 정사각형 개수 학인
for i in range(100) :
    for j in range(100) :
        if graph[i][j] and graph[i+1][j] and graph[i][j+1] and graph[i+1][j+1] :
            result += 1

print(result)