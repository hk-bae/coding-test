import sys
from collections import deque
input = sys.stdin.readline


t = int(input())

result = []
for _ in range(t) :
    n,k = map(int,input().split()) 
    cost = list(map(int,input().split())) # cost[i] 는 i+1 번째 건물의 시간
    graph = [[] for _ in range(n+1)]
    dp = [0] * (n+1)
    indegree = [0] * (n+1)
    for _ in range(k) :
        a,b = map(int,input().split())
        indegree[b] += 1
        graph[a].append(b)

    w = int(input())
    
    q = deque()
    for i in range(1,n+1) :
        if indegree[i] == 0 :
            q.append(i)
            dp[i] = cost[i-1]
            
    while q :
        now = q.popleft()
        
        for i in graph[now] :
            indegree[i] -= 1
            dp[i] = max(cost[i-1] + dp[now], dp[i])
            if indegree[i] == 0 :
                q.append(i)

    result.append(dp[w]) 
            
    
for i in range(t) :
    print(result[i])