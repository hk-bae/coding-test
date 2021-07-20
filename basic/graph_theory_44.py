# https://www.acmicpc.net/problem/2887
# 임의의 두 노드 사이에 터널을 연결할 수 있다고 가정하면 총 N(N-1) / 2 개가 된다.
# N이 최대 100,000이라는 조건을 감안하면 이는 매우 큰 수가 되므로 간선의 개수를 줄일 수 있는 방법을 고안해야 한다.

def find_parent(parent,x) :
    if x != parent[x] :
        parent[x] = find_parent[x]
    return parent[x]

def union_parent(parent,a,b) :
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a > b :
        parent[a] = b
    else :
        parent[b] = a
        
n = int(input())

parent = [0] * (n+1)
for i in range(1,n+1) :
    parent[i] = i
    
edges = [] # (dist,i,j)
result = 0
x = []
y = []
z = []

for i in range(1,n+1) :
    data = list(map(int,input().split()))
    x.append((data[0],i))
    y.append((data[1],i))
    z.append((data[2],i))
    
x.sort()
y.sort()
z.sort()

for i in range(n-1) :
    edges.append((x[i+1][0] - x[i][0], x[i][1],x[i+1][1]))
    edges.append((y[i+1][0] - y[i][0], y[i][1],y[i+1][1]))
    edges.append((y[i+1][0] - y[i][0], y[i][1],y[i+1][1]))
    
edges.sort()

for edge in edges :
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b) :
        union_parent(parent,a,b)
        result += cost
