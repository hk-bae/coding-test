import sys
from collections import deque

input = sys.stdin.readline

def simulate(k) :
    global n
    result = 0
    for t in range(k) :
        alive = []
        dead = []
        addToGraph = []
        # spring
        for i in range(n) :
            for j in range(n) :
                while tree[i][j] :
                    age = tree[i][j].popleft()
                    if graph[i][j] < age :
                        dead.append((age,i,j)) # 양분을 먹지 못하고 죽는다.
                    else :
                        graph[i][j] -= age # 자신의 나이 만큼 양분을 먹는다.
                        alive.append((age+1,i,j)) # 나이 한 살 증가
                        if (age + 1) % 5 == 0 :
                            addToGraph.append((i,j))
                    
        # summer
        for age,x,y in dead :
            graph[x][y] += (age // 2)
    

        # fall
        for x,y in addToGraph :
            for i in range(8) :
                nx = x+dx[i]
                ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n :
                tree[nx][ny].append(1)

        for age,x,y in alive :
            tree[x][y].append(age)
    
        # winter
        for i in range(n) :
            for j in range(n) :
                if t < k-1 :
                    graph[i][j] += a[i][j]
                else :
                    result += len(tree[i][j])
    
    return result
    
n,m,k = map(int,input().split())

# 모든 땅 양분 5로 시작
graph = [[5] * n for _ in range(n)]

a = [list(map(int,input().split())) for _ in range(n)] # 매년 추가되는 양분 

tree = [ [deque() for _ in range(n)]  for _ in range(n)]
dx = [1,-1,0,0,1,-1,1,-1]
dy = [0,0,1,-1,1,-1,-1,1]

tmp = []
for _ in range(m) :
    x,y,z = map(int,input().split())
    tmp.append((z,x,y))

tmp.sort()
for z,x,y in tmp :
    tree[x-1][y-1].append(z)


# k년 동안 진행
result = simulate(k)



print(result)