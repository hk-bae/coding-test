import sys
import copy
input = sys.stdin.readline

# 현재까지 이동 횟수 i
def dfs(i,data) :
    global result

    # 5회 탐색 전
    if i < 5 : 
        for j in range(0,4) :
            if direction[i][j] == False :
                direction[i][j] = True
                # 그래프 이동
                tmp = copy.deepcopy(data)                
                dfs(i+1,move(tmp,j))
                direction[i][j] = False
    else : # 5회 이동 시 최대 값 비교
        max_data = 0
        for i in range(len(data)) :
            for j in range(len(data)) :
                max_data = max(max_data,data[i][j])
        result = max(result,max_data)

def move(data,d) :
    global n 
    
    new_data = [ [0] * n for _ in range(n) ]
    
    if d == 0 : # 상
        # 위에서 아래로 탐색
        i = 1
        j = 0
        next = 0
        previous = data[0][0]
        while i < n and j < n :
            if data[i][j] != 0 :
                if previous == 0 :
                    previous = data[i][j]
                elif data[i][j] == previous : # 서로 같다면
                    new_data[next][j] = previous * 2 # 다음 위치에 두개를 합친 값을 넣는다.
                    next += 1
                    previous = 0
                else : # 서로 다르다면
                    new_data[next][j] = previous
                    previous = data[i][j]
                    next += 1        
            i += 1
            
            # 끝까지 모두 탐색한 경우
            if i == n :
                if previous != 0 : # 남아있는 수가 있다면
                    new_data[next][j] = previous
                j += 1 # 다음 열 탐색
                if j < n :
                    i = 1 # i 초기화
                    previous = data[0][j]
                    next = 0
                         
    elif d == 1 : # 하
        # 아래에서 위로 탐색
        i = n-2
        j = 0
        next = n-1
        previous = data[n-1][0]
        while i >= 0 and j < n  :
            if data[i][j] != 0 :
                if previous == 0 :
                    previous = data[i][j]
                elif data[i][j] == previous : # 서로 같다면
                    new_data[next][j] = previous * 2 # 다음 위치에 두개를 합친 값을 넣는다.
                    next -= 1
                    previous = 0
                else : # 서로 다르다면
                    new_data[next][j] = previous
                    previous = data[i][j]
                    next -= 1        
            i -= 1
            
            # 끝까지 모두 탐색한 경우
            if i == -1 :
                if previous != 0 : # 남아있는 수가 있다면
                    new_data[next][j] = previous
                j += 1 # 다음 열 탐색
                if j < n :
                    i = n-2 # i 초기화
                    previous = data[n-1][j]
                    next = n-1
        
    elif d == 2 : # 좌
        # 좌에서 우로 탐색
        i = 0
        j = 1
        next = 0
        previous = data[0][0]
        while i < n and j < n  :
            if data[i][j] != 0 :
                if previous == 0 :
                    previous = data[i][j]
                elif data[i][j] == previous : # 서로 같다면
                    new_data[i][next] = previous * 2 # 다음 위치에 두개를 합친 값을 넣는다.
                    next += 1
                    previous = 0
                else : # 서로 다르다면
                    new_data[i][next] = previous
                    previous = data[i][j]
                    next += 1        
            j += 1
            
            # 끝까지 모두 탐색한 경우
            if j == n :
                if previous != 0 : # 남아있는 수가 있다면
                    new_data[i][next] = previous
                i += 1 # 다음 행 탐색
                if i < n :
                    j = 1 # j 초기화
                    previous = data[i][0]
                    next = 0
    else : # 우
        # 우에서 좌로 탐색
        i = 0
        j = n-2
        next = n-1
        previous = data[0][n-1]
        while i < n and j >= 0  :
            if data[i][j] != 0 :
                if previous == 0 :
                    previous = data[i][j]
                elif data[i][j] == previous : # 서로 같다면
                    new_data[i][next] = previous * 2 # 다음 위치에 두개를 합친 값을 넣는다.
                    next -= 1
                    previous = 0
                else : # 서로 다르다면
                    new_data[i][next] = previous
                    previous = data[i][j]
                    next -= 1        
            j -= 1
            
            # 끝까지 모두 탐색한 경우
            if j == -1 :
                if previous != 0 : # 남아있는 수가 있다면
                    new_data[i][next] = previous
                i += 1 # 다음 행 탐색
                if i < n :
                    j = n-2 # j 초기화
                    previous = data[i][n-1]
                    next = n-1
        
    return new_data

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
result = 0


# 1회부터 5회까지 상하좌우 탐색 여부
direction = [[False] * 4 for _ in range(5)]

if n == 1 :
    result = graph[0][0] 
else :
    dfs(0,graph)
print(result)