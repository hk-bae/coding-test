# pypy 통과 python3 시간초과

import sys
from collections import deque

input = sys.stdin.readline


def air_cleaner() :
    global R,C,cleaner
    
    x = cleaner # 공기청정기의 위쪽 x좌표
    
    graph[x][0] = 0
    graph[x+1][0] = 0 
    
    # 반시계 방향 바람 불기
    # 아래 방향
    for i in range(x,0,-1) :
        graph[i][0] = graph[i-1][0]

    # 왼쪽 방향
    for j in range(0,C-1) :
        graph[0][j] = graph[0][j+1]
    
    # 위 방향
    for i in range(0,x) :
        graph[i][C-1] = graph[i+1][C-1]

    # 오른쪽 방향
    for j in range(C-1,1,-1) :
        graph[x][j] = graph[x][j-1]
    graph[x][1] = 0

    # 시계방향 바람 불기
    x = x + 1 # 공기청정기 아래 부분으로 이동

    # 위방향
    for i in range(x,R-1) :   
        graph[i][0] = graph[i+1][0]

    # 왼쪽 방향
    for j in range(0,C-1) :
        graph[R-1][j] = graph[R-1][j+1]

    # 아래방향
    for i in range(R-1,x,-1) :
        graph[i][C-1] = graph[i-1][C-1]

    # 오른쪽 방향
    for j in range(C-1,1,-1) :
        graph[x][j] = graph[x][j-1]
    graph[x][1] = 0

    clean = graph[x][0] + graph[x-1][0]
    graph[x][0],graph[x-1][0] = -1,-1

    return clean




R,C,T = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(R)]
cleaner = 0
for r in range(R) :
    if graph[r][0] == -1 :
        cleaner = r # 공기청정기 x좌표 저장
        break

t = 0 # 수행 시간

dx = [0,-1,0,1]
dy = [1,0,-1,0]

while True : 
    # 1. 미세먼지 확산
    tmp = [[0] * C for _ in range(R)] # 확산된 미세먼지 정보
    for x in range(R) :
        for y in range(C) :
            if graph[x][y] < 5 :
                continue # 퍼질 수 없는 경우
            
            spread = graph[x][y] // 5
            cnt = 0 # 미세먼지가 확산된 위치의 수

            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<R and 0<=ny<C and graph[nx][ny] != -1 :
                    cnt += 1
                    tmp[nx][ny] += spread
                
            tmp[x][y] -= (spread * cnt)

    remain = 0 
    # 그래프 갱신
    for i in range(R) :
        for j in range(C) :
            graph[i][j] += tmp[i][j]
            if graph[i][j] != -1 :
                remain += graph[i][j]

    # print("#### after spread ",t+1)
    # for i in range(R) :
    #     for j in range(C) :
    #         print(graph[i][j],end = ' ')
    #     print()

    remain -= air_cleaner() # 공기청정기 동작 수행
    t += 1
    
    # print("#### after clean",t+1)
    # for i in range(R) :
    #     for j in range(C) :
    #         print(graph[i][j],end = ' ')
    #     print()

    if remain == 0 or t >= T :
        break

print(remain)