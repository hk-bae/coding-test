import sys

input = sys.stdin.readline
finish = False

def dfs(x,cnt,k) :
    global n,h,result,finish
    
    if cnt < k :
        for i in range(x,n*h) :
            a = i // n
            b = i % n
            
            # 왼쪽에서 오는 사다리가 있는 경우 사다리를 놓을 수 없다.
            if b > 0 and graph[a][b-1] == 1 :
                continue
            
            # 마지막 위치에는 오른쪽으로 가는 사다리를 놓을 수 없다.
            if b != n-1 and graph[a][b] == 0  :
                graph[a][b] = 1
                dfs(i+1,cnt+1,k)
                graph[a][b] = 0
                if finish : return

    else :
        if play_game() : # 사다리게임 결과 모두 i -> i 이면 result에 k를 담는다.
            result = k
            finish = True
        

def play_game():
    global n,h
    
    result = True
    
    # 모든 열에 대하여
    for start in range(n) :
        j = start 
        for i in range(h) :
            if graph[i][j] == 1 : # 오른쪽으로 가는 사다리
                j += 1
            elif j > 0 and graph[i][j-1] == 1 : # 왼쪽으로 가는 사다리
                j -= 1
        
        if start != j :
            result = False
            break
            
    return result
            
            
    
n,m,h = map(int,input().split())

graph = [[0] * n for _ in range(h)]
result = -1

for _ in range(m) :
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1
    

# 이어지는 사다리가 없는 경우 또는 0개 추가 확인 (기존 상태)
if m == 0 or play_game() :
    print(0)
else :
    # 1,2,3 개에 대하여 각각 추가
    for k in range(1,4) :
        dfs(0,0,k)
        # 하나라도 result가 바뀌게 되면 그 이후는 살펴보지 않는다.
        if result != -1 :
            break
            
    print(result)