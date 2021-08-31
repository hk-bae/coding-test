import sys
import copy

input = sys.stdin.readline

def setAllLocation(location,x,y,setValue) :
    if ((x == 1 or x == 3) and y == 3) or (x == 2 and y == 2) :
        location[1][3] = setValue
        location[2][2] = setValue
        location[3][3] = setValue 
    elif ((x == 1 or x == 3) and y == 4) or (x == 2 and y == 3) :
        location[1][4] = setValue
        location[2][3] = setValue
        location[3][4] = setValue 
    elif ((x == 1 or x == 3) and y == 5) or (x == 2 and y == 4) :
        location[1][5] = setValue
        location[2][4] = setValue
        location[3][5] = setValue 
    elif (x == 0 and y == 20) or ((x == 1 or x == 3) and y == 6) or (x == 2 and y == 5) :
        location[0][20] = setValue
        location[1][6] = setValue
        location[2][5] = setValue
        location[3][6] = setValue 

    return location
        
    

def dfs(cnt,scr,tmp,location) :
    global score

    # 이동 횟수가 10회인 경우 최대 값 갱신
    if cnt == 10 :
        score = max(score,scr)
        return

    # 다음 이동 말 결정
    for i in range(4) :

        # 1. 말을 이동 시키고 점수 증가
        now_x,now_y = tmp[i] # i번째 말의 현재 위치

        # 도착지점에 이미 도착한 말은 선택할 수 없다.
        if now_x == -1 :
            continue

        dx = graph[now_x][now_y][0] # 현재 위치에서 출발했을 때 다음 이동 지점
        dy = orders[cnt] # 주어진 입력만큼 이동

        # 다음 이동 위치
        nx = now_x + dx

        if dx != 0 :
            ny = -1 + dy # 파란색 칸에서 이동을 시작했다면 -1에서 더해준다.
        else :
            ny = now_y + dy
        
        # 이동 위치가 도착 전인 경우
        if (nx == 0 and 0<=ny<21) or (nx == 1 and 0<=ny<7) or (nx==2 and 0<=ny<6) or (nx == 3 and 0<=ny<7):
            # 말이 이동을 마치는 칸에 다른 말이 있으면 그 말은 고를 수 없다.
            if location[nx][ny] != -1 :
                continue
            tmp[i] = [nx,ny]
            location[now_x][now_y] = -1
            location = setAllLocation(location,now_x,now_y,-1)
            location[nx][ny] = i
            location = setAllLocation(location,nx,ny,i)
            dfs(cnt + 1,scr + graph[nx][ny][1],tmp,location)
            tmp[i] = [now_x,now_y]
            location[nx][ny] = -1
            location = setAllLocation(location,nx,ny,-1)
            location[now_x][now_y] = i
            location = setAllLocation(location,now_x,now_y,i)

        else : # 도착지를 넘은 경우
            tmp[i] = [-1,-1] # 도착 표시, 더이상 이동 불가
            location[now_x][now_y] = -1
            location = setAllLocation(location,now_x,now_y,-1)
            dfs(cnt + 1,scr,tmp,location)
            tmp[i] = [now_x,now_y]
            location[now_x][now_y] = i
            location = setAllLocation(location,now_x,now_y,i)


# 윷놀이 판 생성
graph = [[] for _ in range(4)]
location = [ [-1] * 21 for _ in range(4)]

graph[0].append((0,0)) # 시작점
for i in range(1,21) :
    if i*2 == 10 :
        graph[0].append((1,i*2)) # 다음 이동 그래프 번호, 점수
    elif i*2 == 20 :
        graph[0].append((2,i*2)) # 다음 이동 그래프 번호, 점수
    elif i*2 == 30 :
        graph[0].append((3,i*2)) # 다음 이동 그래프 번호, 점수
    else : 
        graph[0].append((0,i*2)) # 다음 이동 그래프 번호, 점수
    

graph[1] = [(0,13),(0,16),(0,19),(0,25),(0,30),(0,35),(0,40)]
graph[2] = [(0,22),(0,24),(0,25),(0,30),(0,35),(0,40)]
graph[3] = [(0,28),(0,27),(0,26),(0,25),(0,30),(0,35),(0,40)]


orders = list(map(int,input().split()))

score = 0 # 점수

horses = [[0,0],[0,0],[0,0],[0,0]] # 말들의 위치

dfs(0,0,horses,location)

print(score)


    




     