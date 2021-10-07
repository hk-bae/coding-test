import sys
input = sys.stdin.readline

# 플로이드 워셜 알고리즘으로 i번 구슬에서 j번 구슬까지의 거리를 graph[i][j]에 표기
# 여기서 거리가 존재한다는 것은 i번 구슬이 j번 구슬보다 가깝고 그 구슬 사이에 dist개의 구슬이 존재한다는 것을 의미한다.

# 모든 거리를 구한 후에 행 별로 그리고 열 별로 탐색을 진행한다.
# mid값보다 큰 값이 존재한다면 해당 구슬은 절대 중간 구슬이 될 수 없다.

n,m = map(int,input().split())
INF = 1e9
graph= [[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(n):
    graph[i][i] = 0
    
for _ in range(m) :
    a,b = map(int,input().split())
    graph[b-1][a-1] = 1
    
for k in range(n) :
    for a in range(n) :
        for b in range(n) :
            if graph[a][b] > graph[a][k] + graph[k][b] :
                graph[a][b] = graph[a][k] + graph[k][b]


result = [False] * n
mid = (n+1) // 2 

# i번째 구슬보다 무거운 구슬이 몇 개인지 확인
for i in range(n) :
    tmp = 0
    for j in range(n) :
        if graph[i][j] != INF and i != j :
            tmp += 1
    if tmp >= (n-mid+1) :
        result[i] = True

# j번째 구슬보다 가벼운 구슬이 몇 개인지 확인
for j in range(n) :
    tmp = 0
    for i in range(n) :
        if graph[i][j] != INF and i != j :
            tmp += 1
    if tmp >= mid :
        result[j] = True

cnt = 0
for x in result :
    if x : cnt += 1
        
print(cnt)
    