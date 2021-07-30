import sys

input = sys.stdin.readline

def find_parent(parent,x) :
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

while True :
    n,m = map(int,input().split())
    if n == 0 and m == 0 :
        break
    graph = [[] for _ in range(n)]
    parent = [i for i in range(n)]
    edges = []

    total_cost = 0
    for _ in range(m) :
        a,b,c = map(int,input().split())
        total_cost += c 
        edges.append((c,a,b))
    
    edges.sort()
    result = 0

    for edge in edges :
        c,a,b = edge
        if find_parent(parent,a) != find_parent(parent,b) :
            union_parent(parent,a,b)
            result += c
        
    result = total_cost - result
    print(result)