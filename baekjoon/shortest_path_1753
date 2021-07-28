import sys
import heapq

input = sys.stdin.readline
INF = 1e9

def dijkstra(start) :
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))

    while q :
        dist,now = heapq.heappop(q)
        
        if dist > distance[now] :
            continue
            
        for i in graph[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
n,e = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
start = int(input())

for _ in range(e) :
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    
dijkstra(start)

for i in range(1,n+1) :
    if distance[i] == INF :
        print('INF')
    else :
        print(distance[i])