import sys

input = sys.stdin.readline

n = int(input())

t = [0] * (n+1)
p = [0] * (n+1)

for i in range(1,n+1) :
    time,paid = map(int,input().split())
    t[i] = time
    p[i] = paid
    
d = [0] * (n+1)

if t[n] == 1 :
    d[n] = p[n]
else :
    d[n] = 0

for i in range(n-1,0,-1) :
    time = t[i] + i
    
    if time - 1 > n :
        d[i] = d[i+1]
    else :
        if time != n + 1 :
          d[i] = max(d[time] + p[i],d[i+1])
        else :
          d[i] = max(p[i],d[i+1])
     
print(d[1])