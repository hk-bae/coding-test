from itertools import combinations

n = int(input())

graph = []

t_array = []
x_array = []

for i in range(n) :
    graph.append(list(input().split()))
    for j in range(n) :
        if graph[i][j] == 'T' :
            t_array.append((i,j))
        elif graph[i][j] == 'X' :
            x_array.append((i,j))
            
def dfs(x,y,i) :
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    nx = x + dx[i]
    ny = y + dy[i]
    
    if 0 <= nx < n and 0 <= ny < n :
        if graph[nx][ny] == 'S' :
            return False
        elif graph[nx][ny] == 'O' :
            return True
        else :
            return dfs(nx,ny,i)
    else :
        return True
        
            
#장애물 3개 조합
candidates = list(combinations(x_array,3))

# answer = True

for c in candidates :
    # 장애물 설치
    graph[c[0][0]][c[0][1]] = 'O'
    graph[c[1][0]][c[1][1]] = 'O'
    graph[c[2][0]][c[2][1]] = 'O'
    
    answer = True
    # 모든 선생님 위치에서 확인
    for x,y in t_array :
        # 네 방향 모두 확인
        for i in range(4) :
            answer = answer and dfs(x,y,i)
            
    if answer :
        break
        
    # 원래대로
    graph[c[0][0]][c[0][1]] = 'X'
    graph[c[1][0]][c[1][1]] = 'X'
    graph[c[2][0]][c[2][1]] = 'X'
    

if answer :
    print("YES")
else :
    print("NO")