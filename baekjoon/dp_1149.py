import sys
input = sys.stdin.readline

def solution(n,house):
    INF = 1e9
    # dp[i][k] : i가 k색 (0:R,1:G,2:B) 일 때 i번째 집까지 칠한 비용의 최솟값 
    dp = [[ INF for _ in range(3)] for _ in range(n)]
    dp[0][0],dp[0][1],dp[0][2] = house[0][0],house[0][1],house[0][2]
    others = [(1,2),(0,2),(0,1)]
    for i in range(1,n) :
        for color in range(3):
            o1,o2 = others[color]
            dp[i][color] = min(dp[i-1][o1],dp[i-1][o2]) + house[i][color]
    
    return min(dp[n-1][0],dp[n-1][1],dp[n-1][2])
    
n = int(input())
house = []
for _ in range(n) :
    r,g,b = map(int,input().split())
    house.append((r,g,b)) # i번째 집의 r,g,b 비용
    
print(solution(n,house))