import sys

input = sys.stdin.readline
INF = 1e9

n,m = map(int,input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1,n+1)  :
    for j in range(1,n+1) :
        if i == j :
            graph[i][j] = 0

for _ in range(m) :
    a,b,c = map(int,input().split())
    graph[a][b] = c
    
for k in range(1,n+1) :
    for i in range(1,n+1) :
        for j in range(1,n+1) :
            if graph[i][j] > graph[i][k] + graph[k][j] :
                graph[i][j] = graph[i][k] + graph[k][j]

min_value = INF

for i in range(1,n+1):
    for j in range(i+1,n+1):
        min_value = min(graph[i][j] + graph[j][i], min_value)
        
if min_value >= INF :
    print('-1')
else :
    print(min_value)