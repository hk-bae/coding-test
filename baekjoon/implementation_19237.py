import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

# 상어 냄새 정보 (상어번호, 사라지는 시간)
area = [[[0,0] for _ in range(n)] for _ in range(n)]

# 상어 위치 정보
location = [[] for _ in range(m+1)]

# 1. 자신의 위치에 냄새 뿌리기
for i in range(n) :
    for j in range(n) :
        if graph[i][j] != 0 :
            area[i][j] = [graph[i][j],k]
            location[graph[i][j]] = [i,j]

# 1,2,3,4 : 상,하,좌,우
dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]

# 각 상어의 현재 방향
direction = [0] + list(map(int,input().split()))

# 각 상어의 방향 우선순위
priority = [[[] for _ in range(5)] for _ in range(m+1)]

for i in range(1,m+1) :
    for j in range(1,5) :
        priority[i][j] = [0] + list(map(int,input().split()))


time = 0
alive = [True] * (m+1) # 생존 목록
alive_cnt = m # 살아있는 상어의 수


while True :

    time += 1 

    empty_area = [[False] * n for _ in range(n)] # 빈공간 체크
    for i in range(n) :
        for j in range(n) :
            if area[i][j] == [0,0] :
                empty_area[i][j] = True

    # 상어 이동
    # 모든 상어에 대해서 탐색
    for i in range(1,m+1) : 
        if alive[i] : # i번째 상어가 살아있는 경우
            x,y = location[i] # 현재 상어의 위치
            now_d = direction[i] # 현재 상어가 바라보는 방향
            
            move = False
            
            # 우선순위 순으로 해당 위치가 비어있는지 탐색
            for j in range(1,5) :

                nx = x + dx[priority[i][now_d][j]]
                ny = y + dy[priority[i][now_d][j]]
                if 0<=nx<n and 0<=ny<n and empty_area[nx][ny]: # 그 위치가 비어있는 공간인 경우
                    if area[nx][ny] == [0,0] :
                        # 상어를 이동
                        area[nx][ny] = [i,time + k] 
                        direction[i] = priority[i][now_d][j] # 바라보는 방향 갱신
                        location[i] = [nx,ny] # 상어 위치 갱신
                        move = True
                        break
                    else : # 더 낮은 번호의 상어가 이미 선점한 경우
                        alive_cnt -= 1
                        alive[i] = False
                        break

            
            # 비어있는 공간이 없다면 자신의 냄새가 있던 공간을 탐색
            if alive[i] and not move : 
                for j in range(1,5) :
                    nx = x + dx[priority[i][now_d][j]]
                    ny = y + dy[priority[i][now_d][j]]
                    if 0<=nx<n and 0<=ny<n and area[nx][ny][0] == i :  # 자신의 냄새가 존재하는 경우
                        # 상어를 이동
                        area[nx][ny][1] = time + k
                        direction[i] = priority[i][now_d][j]
                        location[i] = [nx,ny] # 상어 위치 갱신
                        break

    # 1마리만 살아 남으면 종료
    if alive_cnt == 1 :
        break

    # 1000초가 되면 -1
    if time == 1000 :
        time = -1
        break

    # 상어 냄새 감소
    for i in range(n) :
        for j in range(n) :
            if area[i][j][1] == time : 
                area[i][j] = [0,0] # 냄새 제거

print(time)


