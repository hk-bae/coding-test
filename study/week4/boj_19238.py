import sys
from collections import deque

input = sys.stdin.readline

n,m,f = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n) ] 

start_x,start_y = map(int,input().split()) # 택시 시작 위치
start_x -= 1
start_y -= 1

guest_start = [[0] * n for _ in range(n)]
guest_destination = dict()
for _ in range(m) : # i는 시작 위치 표시, -i는 도착 위치 표시
    s_r,s_c,d_r,d_c = map(int,input().split())
    guest_start[s_r-1][s_c-1] = 1
    guest_destination[(s_r-1,s_c-1)] = (d_r-1,d_c-1)

dx = [1,-1,0,0]
dy = [0,0,1,-1]


guest, res = 0, -1 # 태운 승객 수 , 결과 값

while True :

    # 1.최단거리가 가장 짧은 승객 찾기
    if guest_start[start_x][start_y] == 0  :
        q = deque([(0,start_x,start_y)])
        visited = [[False] * n for _ in range(n)]
        visited[start_x][start_y] = True 
        candidate = [] # 다음 승객 후보군
        next = [] # 다음 이동 위치
        find = False # 승객을 찾았는지 여부
        while q :
            dist,now_x,now_y = q.popleft()
            for i in range(4) :
                nx = now_x + dx[i]
                ny = now_y + dy[i]

                if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and graph[nx][ny] != 1 :
                    visited[nx][ny] = True
                    if guest_start[nx][ny] != 0 : # 승객의 출발지
                        find = True
                        candidate.append((nx,ny))
                    elif graph[nx][ny] == 0 : # 빈공간
                        next.append((dist +1,nx,ny))
                        

            if len(q) == 0:             
                if find : # 다음 위치의 승객을 찾았다면
                    candidate.sort()
                    f -= (dist + 1) # 승객을 찾으러 가는 거리 만큼 연료 감소
                    start_x,start_y = candidate[0][0], candidate[0][1] # 현재 승객의 위치를 시작위치로 변경
                    
                    break
                else : # 승객을 찾지 못했을 경우
                    if len(next) != 0 : # 다음 탐색 위치가 존재하는 경우
                        q = deque(next)
                        next = []
                    else : # 더이상 탐색할 수 있는 위치가 없는 경우
                        f = 0
                        break
        
    if f <= 0 : # 연료가 바닥 나면 실패
        break


    # 2. 손님을 목적지까지 이동
    destination_x,destination_y = guest_destination[(start_x,start_y)]
    guest_start[start_x][start_y] = 0

    q = deque([(start_x,start_y,0)])
    visited = [[False] * n for _ in range(n)]
    visited[start_x][start_y] = True

    while q :
        now_x,now_y,dist = q.popleft()

        if now_x == destination_x and now_y == destination_y : # 목적지 도착
            if f >= dist : # 연료가 충분히 있다면
                f += dist # 충전
                guest += 1  # 손님 이동 성공
                start_x,start_y = now_x,now_y # 다음 출발지 설정
            else :
                f -= dist
            break

        for i in range(4) :
            nx = now_x + dx[i]
            ny = now_y + dy[i]

            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and graph[nx][ny] != 1 :
                visited[nx][ny] = True
                q. append((nx,ny,dist+1))
    
    if guest == m : # 목표 손님 달성
        res = f # 남은 연료의 양
        break

    if f < 0 : # 연료 부족
        break

print(res)



