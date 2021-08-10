import sys
from collections import deque

input = sys.stdin.readline

N,M,K = map(int,input().split())

# 각 칸에 존재하는 파이어볼 (m,s,d) 를 저장할 그래프
# d = 0,1,2,3,4,5,6,7
# d = 8 이면 모든 짝수, d = 9 면 모든 홀수
graph = [[ deque() for _ in range(N)]  for _ in range(N)]
fireball = deque()

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for _ in range(M) :
    r,c,m,s,d = map(int,input().split())
    graph[r-1][c-1].append((m,s,d))
    

# K번 명령 수행
for _ in range(K) :
    # 1. 모든 파이어볼 이동
    for x in range(N) :
        for y in range(N) :
            # 해당 자리에 파이어볼이 존재한다면 이동
            while graph[x][y] : 
                m,s,d = graph[x][y].popleft()
                nx = (x + dx[d] * s) % N
                ny = (y+ dy[d] * s) % N
                fireball.append((nx,ny,m,s,d))

    while fireball :
        x,y,m,s,d = fireball.popleft()
        graph[x][y].append((m,s,d))


    # 2. 2개 이상의 파이어볼이 있는 칸 탐색
    for x in range(N) :
        for y in range(N) :
            total_m = 0 # 전체질량
            total_s = 0 # 전체 속력
            odd_or_even = 0 # 방향
            cnt = 0 # 전체 파이어볼 개수
            
            while graph[x][y] :
                m,s,d = graph[x][y].popleft()
                cnt += 1 
                total_m += m
                total_s += s
                odd_or_even += (d % 2) # 짝수면 0이 더해지고 홀수면 1이 더해진다
            
            # 1개 밖에 없다면 다시 넣는다
            if cnt == 1 :
                graph[x][y].append((m,s,d))
            elif cnt > 1 :
                new_m = total_m // 5
                if new_m == 0 : # 질량이 0이 되면 즉시 소멸시킴
                    continue 
                new_s = total_s // cnt
                # 모두 짝수 혹은 홀수인 경우
                if odd_or_even == cnt or odd_or_even == 0 :
                    for i in range(0,8,2) :
                        graph[x][y].append((new_m,new_s,i))
                else : 
                    for i in range(1,8,2) :
                        graph[x][y].append((new_m,new_s,i))

res = 0

# 남아있는 질량의 합
for x in range(N) :
    for y in range(N) :
        while graph[x][y] :
            m,s,d = graph[x][y].popleft()
            res += m

print(res)
    