import sys

input = sys.stdin.readline
INF = 1e9

def bellman_ford(start) :
    distance[start] = 0
    
    # 전체 n-1번 반복, 마지막 한번은 음수 싸이클 확인
    for i in range(n) :
        # 모든 간선 확인
        for j in range(m) :
            now = edges[j][0]
            next = edges[j][1]
            dist = edges[j][2]
            
            if distance[now] != INF and distance[next] > distance[now] + dist :
                distance[next] = distance[now] + dist
                # 음수 싸이클 판정
                if i == n-1 :
                    return False
    return True
                    

n,m = map(int,input().split())
distance = [INF] * (n+1)
edges = []

for _ in range(m) :
    a,b,c = map(int,input().split())
    edges.append((a,b,c))

if bellman_ford(1) :
    for i in range(2,n+1) :
        if distance[i] == INF :
            print('-1')
        else :
            print(distance[i])
else :
    print('-1')