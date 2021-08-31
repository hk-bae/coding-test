from collections import deque
import sys

input = sys.stdin.readline

N,M,K = map(int,input().split())
res = M # 살아있는 나무의 수

graph = [ [5] * N for _ in range(N)] # 땅의 양분 정보
A = [list(map(int,input().split())) for _ in range(N)] # 겨울에 추가되는 양분의 정보

tree =  [ [deque() for _ in range(N)] for _ in range(N)] # 각 위치의 나무 정보

dx = [1,-1,0,0,1,-1,-1,1]
dy = [0,0,1,-1,1,-1,1,-1]

for _ in range(M) :
    x,y,z = map(int,input().split())
    tree[x-1][y-1].append(z) 

while K > 0 :
    
    alive = deque() # 봄에 조사 후 살아남은 나무들
    fall = [[0] * N for _ in range(N)] # 가을에 번식될 나무의 개수
    for i in range(N) :
        for j in range(N) :
            # 각 나무의 나이에 따라 양분을 준다.
            dead = 0 # (i,j)에서 죽은 나무들로 인해 여름에 더해질 양분의 합
            while tree[i][j] :
                age = tree[i][j].popleft() 
                if graph[i][j] >= age : # 자신의 나이만큼의 양분이 있는 경우
                    alive.append(age+1) # 나이 1 증가
                    graph[i][j] -= age # 원래 위치의 양분 감소
                    if (age+1) % 5 == 0 : # 나이가 5의 배수가 되는 경우
                        for l in range(8) :
                            nx = i + dx[l]
                            ny = j + dy[l]
                            if 0<=nx<N and 0<=ny<N :
                                fall[nx][ny] += 1
                                res += 1
                else : # 양분을 못먹는 경우
                    dead += age // 2 # 여름에 추가될 양분에 추가
                    res -= 1 # 나무 수 감소

            # 다시 살아남은 나무를 tree 큐에 넣는다.
            while alive :
                tree[i][j].append(alive.popleft())

            graph[i][j] += dead # 여름 양분 추가
            graph[i][j] += A[i][j] # 겨울 양분 추가

    for i in range(N) :
        for j in range(N) :
            for k in range(fall[i][j]) :
                tree[i][j].appendleft(1)

    K -= 1



print(res)
