# 2019 카카오 신입 공채 문제

# 소스코드 : 이것이 취업을 위한 코딩테스트다 with 파이썬 513pg

import heapq

def solution(food_times, k):
    answer = 0
    
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1
    
    #시간이 적은 음식부터 빼야 하므로 min heap을 이용
    q = []
    for i in range(len(food_times)) :
        heapq.heappush(q,(food_times[i], i+1)) #(음식시간,음식번호)
    
    sum_value = 0 #먹기 위해 사용한 시간
    previous = 0 #직전에 다 먹은 음식 시간
    
    length = len(food_times) # 남은 음식의 갯수
    
    while sum_value + ((q[0][0] - previous)) * length <= k :
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now
        
    result = sorted(q,key = lambda x : x[1])
    answer = result[(k - sum_value) % length][1]
    return answer


