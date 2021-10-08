n,k = map(int,input().split())

# dp[i][j] : j개를 뽑아서 i가 되는 경우
# dp[i][j] = sum(dp[i][j-l]) # 마지막이 l이 되는 경우
dp = [[0 for _ in range(k+1)] for _ in range(n+1)] 

dp[0][0] = 1
for i in range(n+1) :
    dp[i][1] = 1 
    
for i in range(n+1) :
    for j in range(2,k+1) :
        for l in range(i+1) :
            dp[i][j] += dp[i-l][j-1]
            
print(dp[n][k] % 1000000000)