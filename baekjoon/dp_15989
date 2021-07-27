    
def solution() :
    
    n = int(input())
    
    if dp[n][1] == -1 :
        for i in range(4,n+1) :
            dp[i][1] = dp[i-1][1]
            dp[i][2] = dp[i-2][1] + dp[i-2][2]
            dp[i][3] = dp[i-3][1] + dp[i-3][2]+ dp[i-3][3]
        
    result.append(dp[n][1]+dp[n][2] + dp[n][3])

t = int(input())
result = []

dp = [[-1] * 4 for _ in range(10001)]

dp[1][1] = 1
dp[1][2] = 0
dp[1][3] = 0
dp[2][1] = 1
dp[2][2] = 1
dp[2][3] = 0
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1

for _ in range(t) :
    solution()


for item in result :
    print(item)