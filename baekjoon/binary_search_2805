import sys

input = sys.stdin.readline

n,m = map(int,input().split())
data = list(map(int,input().split()))
data.sort()
start = 0
end = data[-1]

while start <= end :
    mid = (start + end) // 2
    h = 0    
    for i in range(0,n) :
        h += max(0,data[i] - mid)
        
    if h >= m :
        start = mid + 1
        result = mid
    else :
        end = mid - 1
        
print(result)