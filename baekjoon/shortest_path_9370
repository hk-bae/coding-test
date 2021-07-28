import sys
import heapq

input = sys.stdin.readline
INF = 1e9

def solution(case) :
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    graph = [[] * (n+1) for _ in range(n+1)]
    distance = [INF] * (n+1)
    include = [[False,-1] for _ in range(n+1)] 
    for _ in range(m) :
        a,b,d = map(int,input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))
        
    end = [False] * (n+1)
    for _ in range(t) :
        end[int(input())] = True
    
    q = []

    distance[s] = 0
    heapq.heappush(q,(0,s))
    
    while q:
        dist,now = heapq.heappop(q)
        
        if dist > distance[now] :
            continue
    
        for i in graph[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                # now까지 경로에 (g,h)가 포함된 경우 또는 현재 경로가 (g,h)
                if include[now][0] or set([now,i[0]]) == set([g,h]) : 
                    include[i[0]][0] = True
                    include[i[0]][1] = now
                else : # 이전 경로에 (g,h)가 포함되지 않은 경우
                    include[i[0]][0] = False
                    include[i[0]][1] = now
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
            elif cost == distance[i[0]] and (include[now][0] or set([now,i[0]]) == set([g,h])) :
                include[i[0]][0] = True
                include[i[0]][1] = now
                
                for k in range(1,n+1) :
                    if include[k][1] == i[0] :
                        include[k][0] = True
                
  

    for i,isIncluded in enumerate(include) :
        if isIncluded[0] and end[i]:
            result[case].append(i)
    

T = int(input())

result = [[] for _ in range(T)]
for case in range(T) :
    solution(case)

for i in range(T) :
    for v in result[i] :
        print(v,end=' ')
    print()