#https://www.acmicpc.net/problem/1932

n = int(input())
data = [] # n x n 배열
for _ in range(n):
    data.append(list(map(int,input().split())))

#F[(i,j)] = max { F[(i-1,j)], F[(i-1,j-1)] } + data[i][j]
first_down = -1 # data[i-1][j]
second_down = -1 # data[i-1][j-1]


for i in range(1,n) : # 1행 부터
    for j in range(n) : #모든 열에 대해 검사
        if i == j :
            first_down = -1
        else :
            first_down = data[i-1][j]
        
        if j == 0 :
            second_down = -1
        else :
            second_down = data[i-1][j-1]
        
        data[i][j] += max(first_down,second_down)
        
        if i == j : break

result = 0
for j in range(n) :
    result = max(result,data[n-1][j])

print(result)

