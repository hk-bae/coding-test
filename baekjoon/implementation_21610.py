import sys

input = sys.stdin.readline

# 0번 무시, ←, ↖, ↑, ↗, →, ↘, ↓, ↙
# 대각선 2,4,6,8번
dx = [0,0,-1,-1,-1,0,1,1,1]
dy = [0,-1,-1,0,1,1,1,0,-1]

n,m = map(int,input().split())

a = [list(map(int,input().split())) for _ in range(n)]


clouds = [(n-1,0),(n-1,1),(n-2,0),(n-2,1)]

# 각 명령에 대해
for _ in range(m) :
    d,s = map(int,input().split())
    removed = dict()
    # 1. 구름 이동
    for x,y in clouds :
        nx = (x + dx[d] * s) % n
        ny = (y + dy[d] * s) % n
        # 2. 비를 내려 바구니의 물의 양 증가
        a[nx][ny] += 1
        # 3. 구름 제거
        removed[(nx,ny)] = True
        
    # 4. 물복사
    for x,y in clouds :
        x = (x + dx[d] * s) % n
        y = (y + dy[d] * s) % n
        # 대각선 방향 확인
        for i in range(2,9,2) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and a[nx][ny] > 0 :
                a[x][y] += 1  # 바구니의 물의 양 증가
                
    # 5. 새로운 구름 생성
    new_clouds = []
    for i in range(n) :
        for j in range(n) :
            if a[i][j] >= 2 and removed.get((i,j)) == None :
                new_clouds.append((i,j))
                a[i][j] -= 2
    clouds = new_clouds

    
res = 0
# 모든 물 양의 합
for i in range(n) :
    for j in range(n) :
        res += a[i][j]
        
print(res)