import sys
import heapq

input = sys.stdin.readline
r,c,k = map(int,input().split())

A = [[0] * 101 for _ in range(101)] # 1~100 까지  사용

for m in range(1,4) :
    n1,n2,n3 = map(int,input().split())
    A[m][1] = n1
    A[m][2] = n2
    A[m][3] = n3

row = 3
col = 3
res = -1
time = 0


if A[r][c] == k :
    res = 0
else :
    while time < 100 :
        time += 1
        # R연산
        if row >= col :
            col = 2
            # A의 모든 행에 대하여 정렬 수행
            for i in range(1,101) : 
                cnt = [0] * 101 # 1 - 100의 수의 개수를 저장할 배열
                for j in range(1,101) :
                    if A[i][j] == 0 : 
                        continue
                    cnt[A[i][j]] += 1

                q = []
                # 1-99의 수에대한 개수를 heapq에 넣는다.
                # (개수,숫자)
                for m in range(1,101) :
                    if cnt[m] != 0 : 
                        heapq.heappush(q,(cnt[m],m))

                j = 1
                # heapq에서 하나씩 꺼내서 기록
                while q and j < 101:
                    count,num = heapq.heappop(q)
                    A[i][j] = num
                    A[i][j+1] = count
                    j += 2
                
                if j < 101 :
                    for l in range(j,101) :
                        A[i][l] = 0 # 0으로 초기화
                
                col = max(col,j - 1) # 열의 개수 갱신
        # C연산
        else : 
            row = 2 
            # A의 모든 열에 대하여 정렬 수행
            for j in range(1,101) : 
                cnt = [0] * 101 # 1 - 99의 수의 개수를 저장할 배열
                for i in range(1,101) :
                    if A[i][j] == 0 : 
                        continue
                    cnt[A[i][j]] += 1

                q = []
                # 1-99의 수에대한 개수를 heapq에 넣는다.
                # (개수,숫자)
                for m in range(1,101) :
                    if cnt[m] != 0 : 
                        heapq.heappush(q,(cnt[m],m))

                i = 1
                # heapq에서 하나씩 꺼내서 기록
                while q and i < 101:
                    count,num = heapq.heappop(q)
                    A[i][j] = num
                    A[i+1][j] = count
                    i += 2
                
                if i < 101 :
                    for l in range(i,101) :
                        A[l][j] = 0 # 0으로 초기화
                
                row = max(row,i - 1) # 행의 개수 갱신
        
        if A[r][c] == k :
            res = time
            break


print(res)