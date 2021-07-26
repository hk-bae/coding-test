import sys

input = sys.stdin.readline

n,m = map(int,input().split())
time = []

for _ in range(n) :
    time.append(int(input()))
    
time.sort()

start = time[0]
end = time[0] * m

while start <= end :
    mid = (start + end) // 2
    cnt = 0
    for i in range(0,n) :
        cnt += mid // time[i]
        
    if cnt >= m :
        end = mid -1
        result = mid
    else :
        start = mid + 1

print(result)

