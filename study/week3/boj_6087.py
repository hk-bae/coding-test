# python3 시간초과
import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

# 현재 위치, 방향
def dfs(x,y,d):
    global W,H,res

    # 다른 포인트에 도달
    if x == c[1][0] and y == c[1][1] :
        res = visited[x][y]
        # print("###",res)
        # for i in range(H) :
        #     for j in range(W) :
        #         print(graph[i][j],end = ' ')
        #     print()
        return  
    
    # 현 위치의 방향부터 탐색        
    for i in range(d,d+4) :
        nx = x + dx[i%4]
        ny = y + dy[i%4]

        # 범위 내의 벽이 아닌 지점 확인
        if 0<= nx < H and 0 <= ny < W and graph[nx][ny] != '*' :    
            mirror = visited[x][y] # 현 위치 거울의 개수
            if d != i%4 : # 이전 방향이랑 다른 방향
                mirror += 1

            # 현재 거울의 최소 값보다 크거나 같다면 현재 방향에서의 탐색을 종료
            if res <= mirror :
                break

            # 이미 지난적 있는 곳인데 현재 경로보다 더 적은 거울의 개수를 가진 곳이라면 가지 않는다.
            if visited[nx][ny] < mirror :
                continue

            visited[nx][ny] = mirror # 다음 위치 갱신

            # if not (nx == c[1][0] and ny == c[1][1]) :
            #     graph[nx][ny] = '-' # 레이저 표시
                
            dfs(nx,ny,i%4)
    
            # if not(nx == c[1][0] and ny == c[1][1]) :
            #      graph[nx][ny] = '.'


W,H = map(int,input().split())

graph = [list(input().rstrip()) for _ in range(H)]
visited = [[1e9] * W for _ in range(H)]
c = []

tmp = 0
for i in range(H) :
    for j in range(W) :
        if graph[i][j] == 'C' :
            tmp += 1
            c.append((i,j))
        if tmp == 2 :
            break

res = 1e9
dx = [1,0,0,-1]
dy = [0,1,-1,0]

visited[c[0][0]][c[0][1]] = -1 # 방문처리
dfs(c[0][0],c[0][1],-1) 

print(res)
