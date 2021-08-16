import sys
input = sys.stdin.readline

n = int(input())
seats = [[0] * n for _ in range(n)]

students = [ list(map(int,input().split())) for _ in range(n*n) ] # 좋아하는 학생 정보

seats[1][1] = students[0][0] # 첫 학생은 무조건 (1,1)에 앉아야함

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(1,n*n) :
    s,s1,s2,s3,s4 = students[i]
    max_value = 0
    max_empty = 0
    for x in range(n) :
        for y in range(n) :
            # 확인할 자리가 빈자리인 경우 체크
            if seats[x][y] == 0 : 
                cnt = 0 # 좋아하는 학생 인접 수
                empty = 0 # 빈자리
                for d in range(4) :
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0<=nx<n and 0<=ny<n :
                        if  seats[nx][ny] == 0 : # 빈자리
                            empty += 1
                        # 좋아하는 학생 있는 경우
                        elif seats[nx][ny] == s1 or seats[nx][ny] == s2 or seats[nx][ny] == s3 or seats[nx][ny] == s4 : 
                            cnt += 1

                if cnt > max_value : # 현재 인접한 최대 수 보다 크면 갱신
                    max_value = cnt
                    max_empty = empty
                    candidate = (x,y)
                elif cnt == max_value : # 같은 경우 빈자리 수를 비교
                    if empty > max_empty :
                        max_empty = empty
                        candidate = (x,y)
                
    seats[candidate[0]][candidate[1]] = s # 정해진 자리에 학생 앉히기

res = 0
students.sort() # 학생 번호 순으로 정렬
# 만족도 조사
for i in range(n) :
    for j in range(n) :
        s = seats[i][j] # 해당자리에 앉은 학생 번호
        _,s1,s2,s3,s4 = students[s-1] # 해당 학생이 좋아하는 학생 번호
        cnt = 0
        for d in range(4) :
            nx = i + dx[d]
            ny = j + dy[d]
            if 0<=nx<n and 0<=ny<n :
                if seats[nx][ny] == s1 or seats[nx][ny] == s2 or seats[nx][ny] == s3 or seats[nx][ny] == s4 :
                    cnt += 1

        if cnt == 1 :
            res += 1
        elif cnt == 2 :
            res += 10
        elif cnt == 3 :
            res += 100
        elif cnt == 4 :
            res += 1000

print(res)
