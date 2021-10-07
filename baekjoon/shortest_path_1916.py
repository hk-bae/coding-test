import sys
import heapq

input = sys.stdin.readline

def dijkstra(start,end) :
    distance[start] = 0
    q = []
    # 현재 위치 정보를 큐에 삽입
    heapq.heappush(q,(0,start)) # (거리비용,위치)
    
    for destination,cost in graph[start] :
        heapq.heappush(q,(cost,destination))
        
    while q :
        # 현재 큐에서 가장 짧은 간선을 pop
        cost,loc = heapq.heappop(q)
        
        # 이미 정해진 경우
        if distance[loc] < cost :
            continue
        
        # loc에서 시작하는 모든 간선들을 탐색
        for bus in graph[loc] :
            new_cost = cost + bus[1] 
            if distance[bus[0]] > new_cost :
                distance[bus[0]] = new_cost
                heapq.heappush(q,(new_cost,bus[0]))
        
    
    

    
n = int(input())
m = int(input())


# 출발지로부터의 비용 배열
distance = [1e9] * (n+1)

# graph[i] : i번째 도시에서 출발하는 버스의 정보 (도착지,비용)
graph = [[] for _ in range(n+1)] 

for _ in range(m) :
    s,e,cost = map(int,input().split())
    graph[s].append((e,cost))
    
start,end = map(int,input().split())

dijkstra(start,end)
print(distance[end])