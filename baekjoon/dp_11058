n = int(input())

dp = [i for i in range(0,n+1)]

dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 4
dp[5] = 5

for i in range(6,n+1) :
    for j in range(3,6) :
      dp[i] = max(dp[i-j] * (j-1), dp[i]) 

print(dp[n])