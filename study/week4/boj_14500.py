import sys

input = sys.stdin.readline

n,m = map(int,input().split())
graph = [ list(map(int,input().split())) for _ in range(n)]

result = 0

# 1 x 4 모양 확인
for i in range(0,n) :
    for j in range(0,m-3) :
        result = max(result,graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i][j+3])

# 4 x 1 모양 확인
for i in range(0,n-3) :
    for j in range(0,m) :
        result = max(result,graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i+3][j])

# 2 x 2 확인
for i in range(0,n-1) :
    for j in range(0,m-1) :
        result = max(result,graph[i][j] + graph[i+1][j] + graph[i][j+1] + graph[i+1][j+1])

# 2 x 3 확인
for i in range(0,n-1) :
    for j in range(0,m-2) :
        total = graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i+1][j] + graph[i+1][j+1] + graph[i+1][j+2]
        result = max(result,total- graph[i][j+1]-graph[i][j+2],
                    total - graph[i+1][j] - graph[i+1][j+1],
                    total - graph[i+1][j] - graph[i][j+2],
                    total - graph[i][j] - graph[i+1][j+2],
                    total - graph[i+1][j] - graph[i+1][j+2],
                    total - graph[i][j] - graph[i][j+2],
                    total - graph[i][j] - graph[i][j+1],
                    total - graph[i+1][j+1] - graph[i+1][j+2])

# 3 x 2 확인
for i in range(0,n-2) :
    for j in range(0,m-1) :
        total = graph[i][j] + graph[i][j+1] + graph[i+1][j] + graph[i+1][j+1] + graph[i+2][j] + graph[i+2][j+1]
        result = max(result,total - graph[i][j+1] - graph[i+1][j+1],
                    total - graph[i+1][j] - graph[i+2][j],
                    total - graph[i][j+1] - graph[i+2][j],
                    total - graph[i][j] - graph[i+2][j+1],
                    total - graph[i+1][j+1] - graph[i+2][j+1],
                    total - graph[i][j] - graph[i+1][j],
                    total - graph[i][j] - graph[i+2][j],
                    total - graph[i][j+1] - graph[i+2][j+1])
        
print(result)