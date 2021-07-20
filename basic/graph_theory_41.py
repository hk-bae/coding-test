# 이것이 코딩테스트다 393pg

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

graph = [[] for _ in range(n+1)]
for i in range(1,n+1) :
  data = list(map(int,input().split()))
  for j in range(i,n+1) :
    if data[j-1] == 1 :
      graph[i].append(j)

parent = [0] * (n+1)
for i in range(1,n+1) :
  parent[i] = i

for i in range(1,n+1) :
  for j in graph[i] :
    union_parent(parent,i,j)

plan = list(map(int,input().split()))
previous = plan[0]
result = "YES"

for p in plan[1:] :
  if find_parent(parent,p) == find_parent(parent,previous) :
    previous = p
  else :
    result = "NO"
    break

print(result)
