# 아이디어
# 직사각형 2 x 3 , 3 x 2에 대하여 가능한 모든 좌표를 탐색하면서
# 그 안의 모든 원소가 같으면서 빈 공간이 2개인 경우 블럭을 제거해 주었다.
    # 이때 빈 공간에 대해서는 검정 블럭이 떨어질 수 있도록 위에가 뚫려 있어야 한다. -> blank 배열 사용

def solution(board):
    n = len(board)
    
    answer = 0
    removed = 1

    while removed != 0 :
        removed = 0
        blank = [n] * n # blank[k] : k열에서 blank[k]행보다 큰 행으로는 블럭을 떨어트릴 수 없음
        for i in range(n-1) :
            for j in range(n-2) :
                # 가로블록 탐색
                blank_set = set() # 현재 위치 직사각형의 빈 공간 집합
                block_set = set() # 현재 구역의 블록 숫자 집합
                flag = True # 검정 블록 떨어트릴 수 있는지
                
                # 빈공간이 2개이고 구역의 모든 원소가 같아야 한다.
                for m in range(2) :
                    for k in range(3) :
                        if board[i+m][j+k] == 0 : # 빈공간
                            blank_set.add((i+m,j+k))
                        else : # 블럭이 존재
                            blank[j+k] = min(blank[j+k],i+m)
                            block_set.add(board[i+m][j+k])
                        if len(blank_set) > 2 or len(block_set) > 1 :
                            flag = False
                            break
                    if not flag :
                        break

                if flag and len(blank_set) == 2 : # 검정 블럭으로 제거가 가능한 경우

                    canRemove = True
                    for x,y in blank_set :
                        if x >= blank[y]  : # 위에 라인이 비어있지 않은 경우
                            canRemove = False # 제거 불가
                            break

                    if canRemove : 
                        for m in range(0,2) :
                            for k in range(0,3) :
                                if blank[j+k] == i+m :
                                    blank[j+k] = n
                                board[i+m][j+k] = 0 
                        removed += 1
                                  
        for i in range(n-2) :
            for j in range(n-1) :
                # 세로블록 탐색
                blank_set = set() # 현재 위치의 빈 공간
                block_set = set() # 현재 구역의 블록 숫자 집합
                flag = True # 검정 블록 떨어트릴 수 있는지
                for m in range(0,3) :
                    for k in range(0,2) :
                        if board[i+m][j+k] == 0 : # 빈공간
                            blank_set.add((i+m,j+k))
                        else : # 블럭이 존재
                            blank[j+k] = min(blank[j+k],i+m) 
                            block_set.add(board[i+m][j+k])
                        if len(blank_set) > 2 or len(block_set) > 1 :
                            flag = False
                            break
                    if not flag :
                        break

                if flag and len(blank_set) == 2 : # 검정 블럭으로 제거가 가능한 경우

                    canRemove = True
                    for x,y in blank_set :
                        if x >= blank[y] : # 위에 라인이 비어있지 않은 경우
                            canRemove = False # 제거 불가

                    if canRemove : 
                        for m in range(0,3) :
                            for k in range(0,2) :
                                if blank[j+k] == i+m :
                                    blank[j+k] = n
                                board[i+m][j+k] = 0 
                        removed += 1
           
        answer += removed
           
    return answer

print(solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]))