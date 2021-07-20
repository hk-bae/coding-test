#이것이 취업을 위한 코딩테스트다 with 파이썬 527pg
#삼성전자 SW 역량테스트
#https://www.acmicpc.net/problem/15686
from itertools import combinations

n,m = map(int,input().split())
city = []

for i in range(n) :
    city.append(list(map(int,input().split())))

house = [] #집(x,y)
chick = [] #치킨집 (x,y)

for i in range(n) :
    for j in range(n) :
        if city[i][j] == 1 : house.append([i,j])
        elif city[i][j] == 2 : chick.append([i,j])
            

com = list(combinations(chick,m))

min_distance = 1e9

for c_list in com :
    total_distance = 0
    for h in house :
        chick_distance = 1e9 # 해당 집의 치킨 거리
        for c in c_list :
            d = abs(c[0] - h[0]) + abs(c[1] - h[1])
            if chick_distance > d : chick_distance = d
        total_distance += chick_distance
    if min_distance > total_distance : min_distance = total_distance

print(min_distance)


# 527pg 답안예시 코드
from itertools import combinations

n,m = map(int,input().split())
chicken,house = [],[]

for r in range(n) :
    data = list(map(int,input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r,c)) # 일반집
        elif data[c] == 2 :
            chicken.append((r,c)) # 치킨집

candidates = list(combinations(chicken,m))

def get_sum(candidate) :
    result = 0
    for hx,hy in house :
        temp = 1e9
        for cx,cy in candidate :
            temp = min(temp,abs(hx-cx) + abs(hy-cy))
        result += temp
    return result

result = 1e9
for candidate in candidates :
    result = min(result,get_sum(candidate))

print(result)
