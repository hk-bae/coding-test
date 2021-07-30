import sys
from collections import deque

input = sys.stdin.readline

def solution(case) :
    n = int(input())
    indegree = [0] * (n+1) # 진입차수
    graph = [[] for _ in range(n+1)] # 간선 정보
    data = list(map(int,input().split()))
    
    for i in range(n-1) :
        for j in range(i+1,n) :
            indegree[data[j]] += 1
            graph[data[i]].append(data[j])
            
    m = int(input())
    for _ in range(m) :
        a,b = map(int,input().split())
        if graph[a].count(b) != 0 : # 작년에 a의 성적이 더 높은 경우
            indegree[b] -= 1
            indegree[a] += 1
            
            graph[a].remove(b)
            graph[b].append(a)
        else : # 작년에 b의 성적이 더 높은 경우
            indegree[a] -= 1
            indegree[b] += 1
            
            graph[b].remove(a)
            graph[a].append(b)
    
    q = deque()
    
    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1,n+1) :
        if indegree[i] == 0 :
            q.append(i)
    
    if len(q) == 0 :
        result[case] = [0]
        return
    
    while q :
        if len(q) > 1 :
            result[case] = [-1]
            return
        now = q.popleft()
        result[case].append(now)
        
        tmp_cnt = 0
        for i in graph[now] : 
            indegree[i] -= 1
            if indegree[i] == 0 :
                tmp_cnt += 1
                if tmp_cnt > 1 :
                    result[case] = [-1]
                    return
                q.append(i)
                
    if len(result[case]) != n :
        result[case] = [0]


t = int(input())
result = [[] for _ in range(t)]
for case in range(t) :
    solution(case)


for i in range(t) :
    length = len(result[i])
    if length == 1 :
        if result[i][0] == 0 :
            print('IMPOSSIBLE')
        else :
            print('?')
    else :
        for team in result[i] :
            print(team,end= ' ')
        print()