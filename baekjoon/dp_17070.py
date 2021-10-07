n = int(input())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
# 가로 세로 대각
dp = [[[0,0,0] for _ in range(n+1)] for _ in range(n+1)] 

for i in range(n+1) :
    graph[i][0],graph[0][i] = 1,1 # 벽

for i in range(1,n+1) :
    data = list(map(int,input().split()))
    for j in range(n) :
        graph[i][j+1] = data[j]



dp[1][2] = [1,0,0] # 시작 위치

for i in range(1,n+1) :
    for j in range(1,n+1) :
        if graph[i][j] != 1 : # 벽이 아니라면
            # 가로 확인
            dp[i][j][0] += (dp[i][j-1][0] + dp[i][j-1][2])

            # 세로 확인
            dp[i][j][1] += (dp[i-1][j][1] + dp[i-1][j][2])

            # 대각선에서 오는 경우 주변 위치 우선 확인
            if graph[i-1][j] != 1 and graph[i][j-1] != 1 :
                dp[i][j][2] += (dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2])



print(sum(dp[n][n]))