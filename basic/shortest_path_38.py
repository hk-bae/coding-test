#이것이 코딩스트다 pg 575
INF = int(1e9)

n,m = map(int,input().split())

graph = [ [INF] * (n+1) for _ in range(n+1) ]

for i in range(1,n+1) :
  for j in range(1, n+1) :
    if i == j :
      graph[i][j] = 0

for _ in range(m) :
  a,b = map(int,input().split())
  graph[a][b] = 1


for k in range(1,n+1) :
  for i in range(1,n+1) :
    for j in range(1, n+1) :
      graph[i][j] = min(graph[i][j], graph[i][k]+ graph[k][j])

count = 0

for i in range(1,n+1):
  for j in range(1,n+1):
    if graph[i][j] == INF :
      print("INF",end=" ")
    else :
      print(graph[i][j], end =" ")
  print()

for i in range(1,n+1) :
  check = True
  for j in range(1,n+1) :
     if graph[i][j] == INF and graph[j][i] == INF :
       check = False
       break
  if check :
    count += 1

print(count)

