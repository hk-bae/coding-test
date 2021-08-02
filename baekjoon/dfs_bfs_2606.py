from collections import deque

def bfs(v) :
    visited[v] = True
    queue = deque()
    queue.append(v)
    result = 0
    while queue : 
        now = queue.popleft()
        for i in graph[now] :
            if not visited[i] :
                result += 1
                visited[i] = True
                queue.append(i)
                
    return result
    
n = int(input())
e = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(e) :
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    

print(bfs(1))