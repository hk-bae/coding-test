import sys
from collections import deque
input = sys.stdin.readline

# 시작점에서 목표지점까지 target의 중량을 유지하면서 갈 수 있는지 확인
def bfs(start,end,target) :
    
    queue = deque([start])
    visited[start] = True
    while queue :
        now = queue.popleft()
        if now == end :
            return True
            
        for w,v in graph[now] :
            if w >= target and not visited[v] :
                queue.append(v)
                visited[v] = True
                
    return False
           
n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

start = 1e9
end = 0
result = 0
for _ in range(m) :
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
    start = min(c,start)
    end = max(c,end)

for i in range(1,n+1) :
    graph[i].sort(reverse = True)

p1,p2 = map(int,input().split())
visited = [False] * (n+1)
while start <= end :
    mid = (start + end) // 2

    for i in range(1,n+1) :
        visited[i] = False
        
    if bfs(p1,p2,mid) :
        start = mid + 1
        result = mid
    else :
        end = mid - 1
        
print(result)