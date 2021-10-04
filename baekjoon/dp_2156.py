import sys

input = sys.stdin.readline

def solution(n,data) :
    if n == 1 :
        return data[0]
    # dp[i][0] : i번째 음료를 마시는 경우 i번째 포도주까지 마신 최대 양
    # dp[i][1] : i번째 음료를 마시지 않는 경우 i번째 포도주까지 마신 최대 양
    # dp[i][O] =  max(dp[i-2][X] + data[i-1] + data[i], dp[i-1][X] + data[i])
    # dp[i][X] = max(dp[i-1][O], dp[i-1][X])
    dp = [[0 for _ in range(2)] for _ in range(n)]  
    dp[0][0],dp[0][1],dp[1][0],dp[1][1] = data[0],0,data[0]+data[1],data[0]
    
    for i in range(2,n) :
        dp[i][0] = max(dp[i-2][1] + data[i-1] + data[i], dp[i-1][1] + data[i])
        dp[i][1] = max(dp[i-1][0], dp[i-1][1])
        
    return max(dp[n-1][0],dp[n-1][1])

n = int(input())
data = []
for _ in range(n) :
    data.append(int(input()))
    
print(solution(n,data))