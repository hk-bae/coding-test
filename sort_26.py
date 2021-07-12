#https://www.acmicpc.net/problem/1715

import heapq

n = int(input())

data = []
result = 0

for _ in range(n) :
    heapq.heappush(data,int(input())) #최소 힙으로 구현
    
while len(data) != 1 :
    
    cards1 = heapq.heappop(data)
    cards2 = heapq.heappop(data)

    new_cards = cards1 + cards2 # 새로운 카드 묶음
    result += new_cards

    heapq.heappush(data,new_cards)

print(result)
