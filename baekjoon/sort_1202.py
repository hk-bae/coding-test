import heapq
import sys

input = sys.stdin.readline

jewelry = []
bag = []

n,k = map(int,input().split())
for _ in range(n) :
    jewelry.append(list(map(int,input().split())))
    
for _ in range(k) :
    bag.append(int(input()))
    
jewelry.sort() # 무게 순으로 정렬
bag.sort() # 무게 순으로 정렬

# 그리디 알고리즘
# 각 가방에 대해 들어갈 수 있는 최대 가치의 보석을 담는다.
queue = []
result = 0
j = 0

# 모든 가방에 대하여 수행
for i in range(k) :
    # 현재 가방에 들어갈 수 있는 모든 보석에 대하여 반복
    while j < n and jewelry[j][0] <= bag[i] :
        # 최대 힙에 보석의 가치를 넣는다.
        heapq.heappush(queue,-jewelry[j][1])
        j += 1
        
    # 현재 가방에 들어갈 수 있는 최대 가치의 보석을 선택한다.
    # 최대 힙이므로 - 를 붙여준다.
    if queue :
        result -= heapq.heappop(queue)
    
print(result)