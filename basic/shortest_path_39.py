# 이것이 코딩테스트다 390 pg
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m) :
  a,b = map(int,input().split())
  graph[a].append((b,1))
  graph[b].append((a,1))

q = []
heapq.heappush(q,(1,0))

while q :
  now,dist = heapq.heappop(q)
  
  if dist > distance[now] :
    continue

  for i in graph[now] :
    cost = dist + i[1]
    if distance[i[0]] > cost :
      distance[i[0]] = cost
      heapq.heappush(q,(i[0],cost))

index = -1
result = 0
num = 0

for i in range(2,n+1) :
  if distance[i] > result :
    index = i
    result = distance[i]
  elif distance[i] == result :
    num += 1

print(index,result,num)
