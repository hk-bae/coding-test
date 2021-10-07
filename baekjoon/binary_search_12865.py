import sys 
from bisect import bisect_left
from bisect import bisect_right

input = sys.stdin.readline

def solution(n,h,o1,o2) :

    min_value = 1e9
    cnt = 0
    length = n // 2
    if n%2 == 1 : length += 1 # 석순의 총 개수
        
    for i in range(1,h+1): # 개똥벌레가 지나가는 위치 탐색
        tmp = length - bisect_left(o1,i) + bisect_right(o2,i)
        if tmp < min_value :
            min_value = tmp
            cnt = 1
        elif tmp == min_value :
            cnt += 1
        
        
    result = [min_value,cnt]
    
    return result

n,h = map(int,input().split())
o1 = [] # 석순
o2 = [] # 종유석
for i in range(n) :
    if i%2 == 1 :
        o1.append(int(input())) # 개똥벌레가 석순에 부딪히는 마지막 위치
    else :
        o2.append(h-int(input())+1) # 종유석에 개똥벌레가 부딪히기 시작하는 위치

# 이진 탐색을 위해서 석순과 종유석 정렬
o1.sort()
o2.sort()
result = solution(n,h,o1,o2)

print(result[0],result[1])
 
