import sys
from collections import deque

input = sys.stdin.readline

def bfs(x,d) :
    visited[x] = True
    q = deque([(x,d)])
    
    while q :
        now,d = q.popleft()
        left = now - 1 # 왼쪽 톱니
        right = now + 1 # 오른쪽 톱니
        
        if 1 <= left <= 4 and not visited[left]:
            if gear[now][6] != gear[left][2] :
                new_d = -1 if d == 1 else 1
                q.append((left,new_d))
                visited[left] = True

        if 1 <= right <= 4 and not visited[right] :
            if gear[now][2] != gear[right][6] :
                new_d = -1 if d == 1 else 1
                q.append((right,new_d))
                visited[right] = True

        rotate(now,d) # 현재 톱니 회전    
                
# 톱니바퀴 번호, 방향
def rotate(i,d) :
    if d == 1 : # 시계 방향
        tmp = gear[i][7]
        for j in range(0,8) :
            gear[i][j],tmp = tmp,gear[i][j]
            
    else : # 반시계 방향
        tmp = gear[i][0]
        for j in range(7,-1,-1) :
            gear[i][j],tmp = tmp,gear[i][j]
            

gear = [[0] * 8 for _ in range(5)]
for i in range(1,5) :
    data = input()
    for j in range(0,8) :
        gear[i][j] = int(data[j])
        

k = int(input())

for _ in range(k) :
    x,d = map(int,input().split())
    visited = [False] * 5
    bfs(x,d)
    
result = 0

result += (1 if gear[1][0] == 1 else 0)
result += (2 if gear[2][0] == 1 else 0)
result += (4 if gear[3][0] == 1 else 0)
result += (8 if gear[4][0] == 1 else 0)

print(result)