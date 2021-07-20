import heapq

n = int(input())

data = []
for _ in range(n) :
    s,t = map(int,input().split())
    data.append((s,t))

data.sort()

cnt = 1
q = []
heapq.heappush(q,data[0][1])

for i in range(1,n) :
    s,t = data[i]
    min_time = q[0]
    
    if s >= min_time :
        heapq.heappop(q)
    else :
        cnt += 1
        
    heapq.heappush(q,t)
    
print(cnt)