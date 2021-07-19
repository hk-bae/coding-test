#https://www.acmicpc.net/problem/1647
n,m = map(int,input().split())
edges = []

for _ in range(m) :
    a,b,c = map(int,input().split())
    edges.append((c,a,b))

edges.sort()

parent = [0] * (n+1)
for i in range(1,n+1) :
    parent[i] = i

def find_parent(parent,x) :
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b) :
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    
    if a > b :
        parent[a] = b
    else :
        parent[b] = a

max_cost = 0
cost = 0

for edge in edges :
    c,a,b = edge
    # no cycle
    if find_parent(parent,a) != find_parent(parent,b) :
        union_parent(parent,a,b)
        max_cost = c
        cost += c
        
cost -= max_cost
print(cost)
