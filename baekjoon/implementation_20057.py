import sys

input = sys.stdin.readline

# 9도 반시계 방향 회전
def rotate_sand() :
    for i in range(10) : 
        sand_info[i][1],sand_info[i][2] = -sand_info[i][2],sand_info[i][1]

            

N = int(input())

graph = [list(map(int,input().split())) for _ in range(N)]

point_x = N // 2
point_y = N // 2

# 좌 하 우 상
dx = [0,1,0,-1]
dy = [-1,0,1,0]

# 방향에 따라 흩날리는 모래 비율과 이동좌표 dx,dy
sand_info = [[1,-1,1],[1,1,1],
        [7,-1,0],[7,1,0],
        [2,-2,0],[2,2,0],
        [10,-1,-1],[10,1,-1],
        [5,0,-2],
        [0,0,-1]
        ]

d = 0 # 이동방향
move = 1 # 이동할 칸의 수
move_cnt = 0 # move로 이동한 횟수
res = 0

# (0,0) 도달 전까지 반복
while not (point_x == 0 and point_y == 0)  :

    # move 회 이동
    for _ in range(move) :
        # d 방향으로 move 만큼 이동
        point_x += dx[d]
        point_y += dy[d]
        
        sand = graph[point_x][point_y] # 이동한 위치 Y 에 대한 모래 양
        remain_sand = sand
        for p,dsx,dsy in sand_info :
            p_sand = (p * sand) // 100 # 이동할 모래의 양
            if p_sand == 0 : # 이동할 모래가 없다면 패스
                continue
            remain_sand -= p_sand
            nx = point_x + dsx
            ny = point_y + dsy
            if 0 <= nx < N and 0 <= ny < N :
                graph[nx][ny] += p_sand # 모래 이동
            else :
                print(nx,ny,p_sand)
                res += p_sand # 격자 밖으로 모래 이동
        
        # 알파에 해당하는 모래 이동
        nx = point_x + sand_info[-1][1]
        ny = point_y + sand_info[-1][2]

        if 0<= nx < N and 0 <= ny < N :
            graph[nx][ny] += remain_sand
        else :
            print(nx,ny,remain_sand)
            res += remain_sand

         
    move_cnt += 1
    if move_cnt == 2 and move != N-1 : # 마지막 move는 3번 후 종료됨
        move += 1 
        move_cnt = 0
    d = (d + 1) % 4
    rotate_sand()
    print("##",sand_info[-1][1],sand_info[-1][2])
    
print(res)