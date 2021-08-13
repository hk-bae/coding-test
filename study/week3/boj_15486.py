# dp

import sys

input = sys.stdin.readline

n = int(input())

t = [0] * (n+1) 
p = [0] * (n+1)

for i in range(1,n+1) :
    time,paid = map(int,input().split())
    t[i] = time
    p[i] = paid


d = [0] * (n+1) # d[i] - i일에 시작해서 마지막 날까지 낼 수 있는 최대 이익

if t[n] == 1 :  # 마지막 날의 시간이 1이 아니라면 수행할 수 없음 
    d[n] = p[n]
else :
    d[n] = 0

for i in range(n-1,0,-1) :
    time = t[i] + i # 다음 상담을 시작할 수 있는 날짜
    
    if time - 1 > n : # 주어진 기간안에 못끝냄
        d[i] = d[i+1]
    else :
        if time != n + 1 : 
            d[i] = max(d[time] + p[i],d[i+1])
        else : # 주어진 기간에 딱 맞게 해결됨
            d[i] = max(p[i],d[i+1])
            
print(d[1])