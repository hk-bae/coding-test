# https://www.acmicpc.net/problem/14891
# bfs
import sys
from collections import deque

input = sys.stdin.readline

def bfs(x,d) :
    visited[x] = True # 초기 방문 처리
    q = deque([(x,d)])
    
    while q :
        now,d = q.popleft()
        left = now - 1 # 왼쪽 톱니 번호
        right = now + 1 # 오른쪽 톱니 번호
        
        # 왼쪽 톱니바퀴 처리
        if 1 <= left <= 4 and not visited[left]:
            # 현재 톱니의 왼쪽 극과 오른쪽 톱니의 오른쪽 극을 비교
            if gear[now][6] != gear[left][2] :
                new_d = -1 if d == 1 else 1 # 반대 방향 저장
                q.append((left,new_d))
                visited[left] = True

        # 오른쪽 톱니바퀴 처리
        if 1 <= right <= 4 and not visited[right] :
            # 현재 톱니의 오른쪽 극과 왼쪽 톱니의 왼쪽 극을 비교
            if gear[now][2] != gear[right][6] :
                new_d = -1 if d == 1 else 1 # 반대 방향 저장
                q.append((right,new_d))
                visited[right] = True

        rotate(now,d) # 현재 톱니 회전    
                
# 톱니바퀴 번호, 방향
def rotate(i,d) :
    if d == 1 : # 시계 방향 회전, 값을 오른쪽으로 한칸씩 이동
        tmp = gear[i][7]
        for j in range(0,8) :
            gear[i][j],tmp = tmp,gear[i][j]
            
    else : # 반시계 방향, 값을 왼쪽으로 한칸씩 이동
        tmp = gear[i][0]
        for j in range(7,-1,-1) :
            gear[i][j],tmp = tmp,gear[i][j]
            

# 1~4번 톱니의 상태를 저장할 리스트
# 0 - N극, 1 - S극
gear = [[0] * 8 for _ in range(5)] 
for i in range(1,5) :
    data = input()
    for j in range(0,8) :
        gear[i][j] = int(data[j])
        

k = int(input()) # 회전 방법 수

for _ in range(k) :
    x,d = map(int,input().split()) # 톱니 바퀴 번호, 방향(1: 시계, -1 : 반시계)
    visited = [False] * 5 # bfs 탐색을 위해 톱니바퀴의 방문 여부 저장할 배열
    bfs(x,d)
    
result = 0

# 각 톱니바퀴의 12시방향을 확인하고 점수 합산
result += (1 if gear[1][0] == 1 else 0)
result += (2 if gear[2][0] == 1 else 0)
result += (4 if gear[3][0] == 1 else 0)
result += (8 if gear[4][0] == 1 else 0)

print(result)