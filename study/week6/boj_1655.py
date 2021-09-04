# 아이디어
# low_q는 max heap, high_q 는 min heap으로 구현하여 중간 값이 항상 low_q[0]가 되도록 만든다.

import sys
import heapq

input = sys.stdin.readline

n = int(input())

answer = []

low_q,high_q = [],[] # max heap, min heap

low_size,high_size = 1,1

# 항상 low_size <= high_size < low_size + 1 을 유지
# 중간 값은 항상 -low_q[0]


first = int(input()) # 첫번쨰 숫자
answer.append(first)
second = int(input()) # 두번째 숫자
if first > second :
    answer.append(second)
    heapq.heappush(low_q,-second)
    heapq.heappush(high_q,first)
else :
    answer.append(first)
    heapq.heappush(low_q,-first)
    heapq.heappush(high_q,second)


for i in range(n-2) :
    num = int(input()) # 백준이가 외친 숫자

    low = -heapq.heappop(low_q) # low의 가장 큰 숫자
    high = heapq.heappop(high_q) # high의 가장 작은 숫자

    if low_size == high_size : # 큐의 크기가 같으면 무조건 low큐에 삽입
        heapq.heappush(low_q,-low)
        if high >= num : # high가 더 크면 num을 low q에 삽입
            heapq.heappush(low_q,-num)
            heapq.heappush(high_q,high)
        else : # high가 더 작으면 high를 low q에 삽입
            heapq.heappush(low_q,-high)
            heapq.heappush(high_q,num)
        low_size += 1
    else : # low 큐의 크기가 더 큰 경우 high 큐에 삽입
        heapq.heappush(high_q,high)
        if num >= low : # num이 low 보다 크면 num을 high q
            heapq.heappush(high_q,num)
            heapq.heappush(low_q,-low)
        else :
            heapq.heappush(high_q,low)
            heapq.heappush(low_q,-num)
        high_size += 1
    medium = -low_q[0]
    answer.append(medium)

for i in range(n):
    sys.stdout.write(str(answer[i])+"\n") 