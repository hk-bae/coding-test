import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = []

for _ in range(n) :
    graph.append(list(map(int,input().split())))

dp = [[0] * n for _ in range(n)]

dp[0][0] = 1

for i in range(n) :
    for j in range(n) :
        distance = graph[i][j]
        if distance == 0 :
            continue
        if i + distance < n :
            dp[i+distance][j] += dp[i][j]
        
        if j + distance < n :
            dp[i][j+distance] += dp[i][j]
        
print(dp[-1][-1])