import sys

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
    
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [i for i in range(n+1)]

m = int(input())
edges = []
for _ in range(m) :
    a,b,c = map(int,input().split())
    if a != b :
        edges.append((c,a,b))
        
edges.sort()
result = 0


for edge in edges :
    c,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b) :
        union_parent(parent,a,b)
        result += c 
        
print(result)