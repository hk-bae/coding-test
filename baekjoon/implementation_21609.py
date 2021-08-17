import sys
from collections import deque

n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

score = 0 

# 블록 그룹이 존재할때 까지 반복
while True : 
    visited = [[False] * n for _ in range(n)]
    max_size,max_rainbow = 0,0 # 최대 크기, 최대크기일때 무지개 블럭 개수
    standard_x,standard_y = 0,0 # 기준 블록
    block_group = [] # (x,y)

    # 1. 크기가 가장 큰 블록 그룹 찾기
    for i in range(n) :
        for j in range(n) :
            # 아직 그룹이 형성되지 않은 블록 중 일반 블록에서 부터 시작
            if not visited[i][j] and graph[i][j] >= 1 and graph[i][j] <= m :
                visited[i][j] = True
                q = deque([(i,j)])
                tmp_size,tmp_rainbow = 1,0
                tmp_group = [(i,j)]
                rainbow_group = []
                value = graph[i][j] # 찾아야할 색상
                tmp_x,tmp_y = i,j # 현재 그룹의 기준 블럭

                while q :
                    now_x,now_y = q.popleft()
                    for d in range(4) :
                        nx = now_x + dx[d]
                        ny = now_y + dy[d]
                        #  인접한 같은 색상 또는 무지개 블럭을 추가
                        if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and (graph[nx][ny] == 0 or graph[nx][ny] == value):
                            visited[nx][ny] = True
                            q.append((nx,ny))
                            tmp_group.append((nx,ny)) # 현재 블록 그룹 저장
                            tmp_size += 1 
                            if graph[nx][ny] == 0 : # 무지개블록인지 확인
                                tmp_rainbow += 1
                                rainbow_group.append((nx,ny))
                            else :
                                # 기준 블록이 변화하는지 확인.
                                if tmp_x > nx or (tmp_x == nx and tmp_y > ny) :
                                    tmp_x = nx
                                    tmp_y = ny    
                                
                                    


                # 무지개 블록은 다른 블록그룹에 포함될 수 있음으로 방문 False 처리
                for x,y in rainbow_group :
                    visited[x][y] = False

                # 2보다 작은 크기는 블록이 아직 형성되지 않은 것
                if tmp_size < 2 :
                    continue
                
                # 가장 큰 블록 그룹과 비교
                if tmp_size > max_size : # 크기 우선 비교
                    max_size,max_rainbow,block_group,standard_x,standard_y = tmp_size,tmp_rainbow,tmp_group,tmp_x,tmp_y
                elif tmp_size == max_size : # 크기가 같을 경우
                    if tmp_rainbow > max_rainbow : # 무지개 블록 개수 비교
                        max_size,max_rainbow,block_group,standard_x,standard_y = tmp_size,tmp_rainbow,tmp_group,tmp_x,tmp_y
                    elif tmp_rainbow == max_rainbow : # 무지개 블록 개수도 같을 경우
                        if standard_x < tmp_x or (standard_x == tmp_x and standard_y < tmp_y) : # 행,열 비교
                            max_size,max_rainbow,block_group,standard_x,standard_y = tmp_size,tmp_rainbow,tmp_group,tmp_x,tmp_y
                        
                         
            
    # 더이상 블록이 남아있지 않는 경우
    if max_size == 0 : 
        break

    # 2. 1에서 찾은 블록 제거
    for x,y in block_group :
        graph[x][y] = -2

    score += pow(max_size,2)
    
    # print("after remove")
    # for i in range(n) :
    #     for j in range(n) :
    #         print(graph[i][j],end = ' ' )
    #     print()

    #3. 격자 중력 작용
    after_gravity = [[-2] * n for _ in range(n)]
    for j in range(n) :
        next = n-1
        for i in range(n-1,-1,-1) :
            if graph[i][j] != -1 and graph[i][j] != -2 : # 일반 블록, 무지개 블록인 경우
                after_gravity[next][j] = graph[i][j]
                next -= 1
            elif graph[i][j] == -1 : # 검정블록인 경우
                next = i - 1
                after_gravity[i][j] = -1

    # print("after gravity")
    # for i in range(n) :
    #     for j in range(n) :
    #         print(after_gravity[i][j],end = ' ' )
    #     print()

    #4. 90 도 반시계 회전
    after_rotate = [[-2] * n for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            after_rotate[n-j-1][i] = after_gravity[i][j]

    # print("after rotate")
    # for i in range(n) :
    #     for j in range(n) :
    #         print(after_rotate[i][j],end = ' ' )
    #     print()

    #5. 격자 중력 작용
    after_gravity = [[-2] * n for _ in range(n)]
    for j in range(n) :
        next = n-1
        for i in range(n-1,-1,-1) :
            if after_rotate[i][j] != -1 and after_rotate[i][j] != -2 : # 일반 블록, 무지개 블록인 경우
                after_gravity[next][j] = after_rotate[i][j]
                next -= 1
            elif after_rotate[i][j] == -1 : # 검정블록인 경우
                next = i - 1
                after_gravity[i][j] = -1
    
    # 다시 그래프로 복사
    for i in range(n) :
        for j in range(n) :
            graph[i][j] = after_gravity[i][j]

    # print("after gravity2")
    # for i in range(n) :
    #     for j in range(n) :
    #         print(graph[i][j],end = ' ' )
    #     print()


print(score)