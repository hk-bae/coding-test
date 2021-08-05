# https://www.acmicpc.net/problem/2839
# dp
import sys

input = sys.stdin.readline

n = int(input())

# F(n) = min{ F(n-3), F(n-5) } + 1 (n > 5)
INF = 1e9
d = [1e9] * (n+1)

if n < 3 :
    print(-1)
elif n == 3 :
    print(1)
elif n < 5 :
    print(-1)
elif n == 5 :
    print(1)
else :
    d[3] = 1
    d[5] = 1
    
    for i in range(6,n+1) :
        d[i] = min(d[i-3],d[i-5]) + 1
    
    result = d[n] if d[n] < INF else -1
    print(result)