import sys

input = sys.stdin.readline


n,l = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]
result = 0

# 가로 길 확인
for i in range(0,n) :
    previous = graph[i][0] # 이전 길의 높이
    cnt = 1 # 현재 높이의 개수
    down = False # 내리막
    success = True # 사용 가능한 길인지
    for j in range(1,n) :
        if down : # 내리막인 경우
            # 이전 길과 현재 높이가 다르다면 실패
            if previous != graph[i][j] :
                success = False
                break
            cnt += 1 
            if l == cnt :
                down = False
                cnt = 0
            continue
       
        # 이전 높이가 현재와 같은 경우
        if previous == graph[i][j] : 
            cnt += 1 # 현재 높이 개수 증가
        elif graph[i][j] - previous == 1 : # +1의 오르막
            if l <= cnt :
                previous = graph[i][j]
                cnt = 1
            else :# 충분한 바닥면이 없다면 실패
                success = False
                break 
        elif graph[i][j] - previous == -1 : # -1의 내리막
            previous = graph[i][j]
            if l != 1 : # 경사로 길이가 1이 아니라면
                cnt = 1
                down = True # 다음 길부터 내리막 경사로를 올바르게 설치할 수 있는지 확인
            else :
                cnt = 0    
        else : # 높이가 2이상 차이 나는 경우 실패
            success = False
            break
            
    if success and not down :
        result += 1 

# 세로 길 확인
for j in range(0,n) :
    previous = graph[0][j] # 이전 길의 높이
    cnt = 1 # 현재 높이의 개수
    down = False # 내리막
    success = True # 사용 가능한 길인지
    for i in range(1,n) :
        if down : # 내리막인 경우
            # 이전 길과 현재 높이가 다르다면 실패
            if previous != graph[i][j] :
                success = False
                break
            cnt += 1 
            if l == cnt :
                down = False
                cnt = 0
            continue
       
        # 이전 높이가 현재와 같은 경우
        if previous == graph[i][j] : 
            cnt += 1 # 현재 높이 개수 증가
        elif graph[i][j] - previous == 1 : # +1의 오르막
            if l <= cnt :
                previous = graph[i][j]
                cnt = 1
            else :# 충분한 바닥면이 없다면 실패
                success = False
                break 
        elif graph[i][j] - previous == -1 : # -1의 내리막
            previous = graph[i][j]
            if l != 1 : # 경사로 길이가 1이 아니라면
                cnt = 1
                down = True # 다음 길부터 내리막 경사로를 올바르게 설치할 수 있는지 확인
            else :
                cnt = 0    
        else : # 높이가 2이상 차이 나는 경우 실패
            success = False
            break

    if success and not down:
        result += 1 

print(result)