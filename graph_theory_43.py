# 이것이 코딩테스트다 pg 397
# University of UIm Local Contest
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

n,m = map(int,input().split())
parent = [0] * n
for i in range(n) :
  parent[i] = i

edges = []
for _ in range(m) :
  x,y,z = map(int,input().split())
  edges.append((z,x,y))

edges.sort()
total_cost =0
cost = 0
for edge in edges :
  z,x,y = edge
  total_cost += z
  if find_parent(parent,x) != find_parent(parent,y) :
    union_parent(parent,x,y)
    cost += z
  
print(total_cost - cost)
