import sys
input = sys.stdin.readline

def solution(n,k,weights,values) :
    # dp[i][j] : i번째 물건을 포함시킬때 j 가방에 담을 수 있는 최대 가치
    # dp[i][j] = max(dp[i-1][j-w[i]] + v[i], dp[i-1][j]) -> i번째를 포함시키는 경우와 포함시키지 않는 경우 중 최댓값
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    
    for i in range(1,n+1) :
        for j in range(1,k+1):
            if j - weights[i] < 0 :
                dp[i][j] = dp[i-1][j]
                continue
            dp[i][j] = max(dp[i-1][j-weights[i]] + values[i], dp[i-1][j])
            
    return dp[n][k]

n,k = map(int,input().split())
weights = [0] * (n+1)
values = [0] * (n+1)
for i in range(n) :
    weights[i+1],values[i+1] = map(int,input().split())
    
result = solution(n,k,weights,values)

print(result)
