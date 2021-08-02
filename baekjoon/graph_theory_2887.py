import sys

input = sys.stdin.readline

def find_parent(parent, x) :
    if x != parent[x] :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b) :
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    
    if a > b :
        parent[a] = b
    else :
        parent[b] = a

n = int(input())
parent = [i for i in range(n)]
planets = []
edges = []

for i in range(n) :
    x,y,z = map(int,input().split())
    planets.append((i,x,y,z))
    
# x좌표에 대한 정렬
planets.sort(key = lambda x : x[1])

for i in range(n-1) :
    cost = planets[i+1][1] - planets[i][1]
    edges.append((cost,planets[i][0],planets[i+1][0]))
    
# y좌표에 대한 정렬
planets.sort(key = lambda x : x[2])

for i in range(n-1) :
    cost = planets[i+1][2] - planets[i][2]
    edges.append((cost,planets[i][0],planets[i+1][0]))
    
# z좌표에 대한 정렬
planets.sort(key = lambda x : x[3])

for i in range(n-1) :
    cost = planets[i+1][3] - planets[i][3]
    edges.append((cost,planets[i][0],planets[i+1][0]))



# 비용 순으로 정렬
edges.sort()

cnt = 0
result = 0

for edge in edges :
    if cnt == n - 1 : break
    c,a,b = edge
    # 사이클이 형성되지 않을 경우만
    if find_parent(parent,a) != find_parent(parent,b) :
        union_parent(parent,a,b)
        cnt += 1
        result += c
        
print(result)