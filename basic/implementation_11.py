       
def tailDirection(board,tail_x,tail_y) :
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    n = len(board)
    for i in range(4) :
        x = tail_x + dx[i]
        y = tail_y + dy[i]
        if 0 <= x < n and 0 <= y < n :
            if board[x][y] == 2 : return i
            
    return -1 

n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수

board = [[0] * n for _ in range(n)]

for _ in range(k) :
    i,j = map(int,input().split())
    board[i-1][j-1] = 1 # 사과의 위치
    
l = int(input()) #방향 전환 횟수

direction_changed = {}

for _ in range(l) :
    secStr,direction = input().split()
    sec = int(secStr)
    direction_changed[sec] = direction
    
head_x = 0
head_y = 0

tail_x = 0
tail_y = 0

board[0][0] = 2

end_time = 0

direction_now = 0

dx = [0,1,0,-1]
dy = [1,0,-1,0]


while True :
    if end_time in direction_changed :
        d = direction_changed[end_time]
        if d == 'L' :
            direction_now = (direction_now - 1) % 4
        else : #'D'
            direction_now = (direction_now + 1) % 4
    
    head_x += dx[direction_now]
    head_y += dy[direction_now]
    
    #벽에 부딪히는 경우
    if head_x >= n or head_x < 0 or head_y >= n or head_y < 0 :
        end_time += 1
        print("case1")
        break
    elif board[head_x][head_y] == 2 and head_x != tail_x and head_y != tail_y : # 자기 자신의 몸과 부딪히는 경우        
        end_time += 1
        print("case2")
        print(str(head_x)+","+str(head_y))
        print(str(tail_x)+","+str(tail_y))
        print(board[head_x][head_y])
        break
    elif board[head_x][head_y] == 1 : #사과를 만나는 경우
        board[head_x][head_y] = 2 # 꼬리가 줄어들지 않음
    else : #사과가 없는 경우
        board[head_x][head_y] = 2
        board[tail_x][tail_y] = 0
        td = tailDirection(board,tail_x,tail_y)
        tail_x += dx[td]
        tail_y += dy[td]
      
    print(str(head_x)+" "+str(head_y))

    end_time += 1
    
          
print(end_time)      
