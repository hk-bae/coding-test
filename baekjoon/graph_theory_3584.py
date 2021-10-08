import sys
from collections import deque 
input = sys.stdin.readline


t = int(input())
for _ in range(t) :
    n = int(input())
    level = [0] * (n+1) # 각 노드의 레벨 저장
    parent = [0] * (n+1) # 각 노드의 부모 노드 번호 저장
    graph = [[] for _ in range(n+1)] # 각 노드의 자식 노드 번호
    indegree = [0] * (n+1) # 최고 조상 찾기 위한 진입차수

    for _ in range(n-1) :
        p,c = map(int,input().split()) 
        parent[c] = p # c의 부모는 p
        graph[p].append(c) # 자식 노드 추가
        indegree[c] += 1 

    a,b = map(int,input().split()) # 두 노드 

    # 루트 찾기
    root = 0
    for i in range(1,n+1) :
        if indegree[i] == 0 :
            root = i
            break 

    level[root] = 1

    q = deque([(root,1)])
    # 각 노드의 레벨 정의
    while q :
        now,lv = q.popleft()
        for i in graph[now] :
            level[i] = lv + 1 
            q.append((i,lv+1))
        
    # a,b에서부터 부모로 거슬러 올라가며 최소 공통조상 찾기
    while a != b:
        if level[a] > level[b] :
            a = parent[a]
        elif level[a] < level[b]:
            b = parent[b]
        else :
            a = parent[a]
            b = parent[b]

    
    print(a)