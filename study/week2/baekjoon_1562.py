# https://www.acmicpc.net/problem/1562
# dfs, bitmask

n = int(input())
mod = 1000000000 # 나눠줄 수
#d[i][j][k]
# i자리수일 때 j로 끝나면서 k 비트정보를 갖는 수의 개수 
d = [[[0] * (1 << 10) for _ in range(10)] for _ in range(n+1)]

# 한 자리수 일때 j(1~9)로 끝나는 수에 대하여 갱신
for j in range(1,10) : # 0으로 시작하는 수는 없다.
    d[1][j][1<<j] = 1

# n자리 수가 될때 까지 반복
for i in range(1,n):
    # j로 끝나는 수에 대하여

    for j in range(10) :  
        for bitmask in range(1<<10) :
            # 0으로 끝나는 수를 제외하고 자신보다 큰 수에서 끝나는 수에서 올라오는 계단 수
            if j != 0 :
                d[i+1][j][bitmask | (1<<j)] += d[i][j-1][bitmask] % mod
            if j != 9 :
                d[i+1][j][bitmask | (1<<j)] += d[i][j+1][bitmask] % mod

result = 0
for j in range(10) :
    result += d[n][j][(1<<10) -1]

print(result)