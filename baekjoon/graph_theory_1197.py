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
        
    return parent

def krusckal(v,edges) :
    parent = [ i for i in range(v+1)]
    
    weight = 0
    for edge in edges :
        cost,a,b = edge
        # 사이클
        if find_parent(parent,a) == find_parent(parent,b) :
            continue
        
        parent = union_parent(parent,a,b)
        weight += cost
        
    return weight
        
v,e = map(int,input().split())
edges = []
for _ in range(e) :
    a,b,c = map(int,input().split())
    edges.append((c,a,b))
    
    
edges.sort()

print(krusckal(v,edges))
