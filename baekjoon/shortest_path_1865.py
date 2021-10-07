import sys 
input = sys.stdin.readline
# 벨만포드에서 distance[now] != INF 를 체크하지 않고 가중치가 줄어드는지만 체크하는 방법으로 구현하면
# find union을 사용할 필요 없다.

# 벨만포드 알고리즘을 사용하여 임의의 지점에서 모든 지점X로 이동하는 distance 구하기
# 만약 사이클이 존재한다면 시간을 되돌릴 수 있다
def solution(start,n,edges) :
    INF = 1e9
    distance = [INF] * (n+1)
    distance[start] = 0
    
    for i in range(n+1) :
        for edge in edges :
            cost,now,other = edge
            if distance[now] != INF and distance[now] + cost < distance[other] :
                if i == n :
                    return True # 사이클 생성
                distance[other] = distance[now] + cost
    
    return False


def find_parent(parent,x) :
    if parent[x] != x :
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

result = []

tc = int(input())
for _ in range(tc) :
    n,m,w = map(int,input().split()) # 정점, 양의간선, 음의간선 개수
    parent = [ i for i in range(n+1)]
    edges = []
    for _ in range(m) :
        a,b,cost = map(int,input().split())
        edges.append((cost,a,b))
        edges.append((cost,b,a))
        union_parent(parent,a,b)
        
    for _ in range(w) :
        a,b,cost = map(int,input().split())
        edges.append((-cost,a,b))
        union_parent(parent,a,b)
       
    for i in range(1,n+1) :
        isCycle = False
        if parent[i] == i :
            if solution(i,n,edges) :
                isCycle = True
                break
    result.append(isCycle)    
        
        
for isCycle in result :
    if isCycle :
        print("YES")
    else :
        print("NO")