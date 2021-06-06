#21. 인구이동
#https://www.acmicpc.net/problem/16234
from collections import deque

n,l,r = map(int,input().split()) # nxn 땅의 크기, l명 이상 r명 이하

a = [] #나라의 인구 수
for _ in range(n) :
    a.append(list(map(int,input().split())))
    
# visited[k]는 (i,j) 국가를 방문했는지 여부 k = i * n + j
# i = k // n, j = k % n
visited = [False] * n * n 

count = 0 # 인구 이동 발생 횟수
move = False

def bfs(i,j) :
    global move
    queue = deque([(i,j)])
    
    k = i * n + j
    visited[k] = True

    sum = a[i][j]

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    countries = [(i,j)]
  

    while queue :
        x,y = queue.popleft()
        # 상하좌우 모두 확인
        for d in range(4) :
            nx = x + dx[d]
            ny = y + dy[d]
          
            if 0 <= nx < n and 0 <= ny < n : # 범위 내에 있으면
                k = nx * n + ny
                #아직 방문하지 않았으면 
                if not visited[k] :
                    if check(a[x][y],a[nx][ny]) : #국경선이 열릴 수 있으면 추가 
                        queue.append((nx,ny))
                        visited[k] = True # 방문 표시
                        sum += a[nx][ny]
                        countries.append((nx,ny))
    
    if len(countries) > 1 :
        move = True
        tmp = sum // len(countries)
        for i,j in countries :
            a[i][j] = tmp
        
    
    
    
#두 지역 간 인구 차이가 l이상 r이하라면 국경선이 열린다.
def check(c1,c2) :
    sub = abs(c1 - c2)
    if l <= sub <= r :
        return True
    return False



while True : 
    move = False
    for i in range(n) :
        for j in range(n) :
            k = i * n + j
            if visited[k] : # 이미 방문 했다면 다음 도시 확인
                continue 
            bfs(i,j) # (i,j)를 기준을 탐색 시작

    if move : #이동이 있었다면
        count +=1
        visited = [False] * n * n 
        move = False
    else :
        break # 종료
        
print(count)
