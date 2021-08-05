# https://programmers.co.kr/learn/courses/30/lessons/72413
# floyd

def solution(n, s, a, b, fares):
    INF = 1e9 # 무한
    graph = [[INF] * (n+1) for _ in range(n+1)] # 이동 정보를 담을 그래프
    
    for c,d,f in fares : 
        graph[c][d] = f # c에서 d로 가는 요금이 f이다
        graph[d][c] = f # d에서 c로 가는 요금이 d이다
        
    for i in range(1,n+1) :
        for j in range(1,n+1) :
            if i == j :
                graph[i][j] = 0 # 자기 자신으로 가는 비용은 0으로 초기화
        
    # floyd algotihm
    for k in range(1,n+1) :
        for i in range(1,n+1) :
            for j in range(1,n+1) :
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                

    # 최소 비용 찾기
    # <s -> x> + <x-> a> + <x-> b>
    # <s -> a + s -> b>
    
    min_cost = graph[s][a] + graph[s][b] # 합승하지 않는 경우
    for x in range(1,n+1) :
        cost = graph[s][x] + graph[x][a] + graph[x][b]
        min_cost = min(cost,min_cost)
        
    return min_cost