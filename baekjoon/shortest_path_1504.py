import sys
import heapq

input = sys.stdin.readline
INF = 1e9

def dijkstra(start,end) :
    global n
    distance = [INF] * (n+1)
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
                
    return distance[end]
     
n,e = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e) :
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
v1,v2 = map(int,input().split())

path_1 = dijkstra(1,v1) + dijkstra(v1,v2) + dijkstra(v2,n)
path_2 = dijkstra(1,v2) + dijkstra(v2,v1) + dijkstra(v1,n)

shortest_path = min(path_1,path_2)

print(shortest_path) if shortest_path < INF else print(-1)