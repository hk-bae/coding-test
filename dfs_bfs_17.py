# https://www.acmicpc.net/probelm/18405

import heapq

n,k = map(int,input().split())

data = [[0] * (n+1) for _ in range(n+1)]
for i in range(1,n+1) :
    tmp = list(map(int,input().split()))
    for j in range(1,n+1):
        data[i][j] = tmp[j-1]

s,x,y = map(int,input().split())

virus = [] #(num,x,y)
for i in range(1,n+1) :
    for j in range(1,n+1):
        if data[i][j] != 0 :
            virus.append((data[i][j],i,j))

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

h = []
#최소 힙에 각 바이러스 데이터 추가
for value in virus :
    heapq.heappush(h,value)

time = 0
#s초 까지 반복
while time < s and len(h) > 0 :
    tmp = []
    for _ in range(len(h)) :
        v = heapq.heappop(h)
        num = v[0] #바이러스 번호
        vx = v[1] #바이러스의 x좌표
        vy = v[2] #바이러스의 y좌표
        for i in range(4) :
            nx = vx + dx[i]
            ny = vy + dy[i]
            if 0 < nx <= n and 0 < ny <= n :
                if data[nx][ny] == 0 :
                    data[nx][ny] = num
                    tmp.append((num,nx,ny)) #바이러스 추가
    for virus in tmp :
        heapq.heappush(h,virus)
    time += 1

print(data[x][y])
