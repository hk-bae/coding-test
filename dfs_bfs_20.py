from itertools import combinations
n = int(input())

school = [] #전체 학교 복도
x = [] # 빈공간
t = [] #선생님

for i in range(n) :
    school.append(list(input().split()))

for i in range(n) :
    for j in range(n) :
        if school[i][j] == 'X' :
            x.append((i,j)) # 빈 공간 위치 추가
        elif school[i][j] == 'T' :
            t.append((i,j)) #선생님 위치 추가


def dfs(x,y,d):
    dx = [1,-1,0,0] 
    dy = [0,0,1,-1]
    
    nx = x + dx[d]
    ny = y + dy[d]
    
    if 0 <= nx < n and 0 <= ny < n :
        if tmp[nx][ny] == 'S' :
            return False # 실패
        elif tmp[nx][ny] =='O' :
            return True
        else :
            return dfs(nx,ny,d)
    else :
        return True 

def copy() :
  for i in range(n) :
    for j in range(n) :
      tmp[i][j] = school[i][j]





x_candidates = list(combinations(x,3)) # 빈 공간중 3개를 고르는 조합
tmp = [[''] * n for _ in range(n)]
result = "YES"

for candidate in x_candidates :
    copy() #학교 복도 복사

    for x,y in candidate : # 각 장애물 추가
        tmp[x][y] = 'O'
    
    result = 'YES'

    for tx,ty in t : # 각 선생님 확인
        for d in range(4) : # 상하좌우 확인
            if not dfs(tx,ty,d) : #실패
                result = 'NO'
                break
        if result == 'NO' : break
    
    if result == 'YES' : break
        
    
print(result)
