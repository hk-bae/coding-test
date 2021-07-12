#이것이 취업을 위한 코딩테스트다 with 파이썬 561pg
#https://www.acmicpc.net/problem/2110

n,c = list(map(int,input().split(' ')))

array = []

for _ in range(n) :
    array.append(int(input()))
array.sort()

start = 1
end = array[-1] - array[0] # 가능한 최대 거리
result = 0

while(start <= end) :
    mid = (start + end) // 2
    value = array[0]
    count = 1
    
    for i in range(1,n) :
        if array[i] >= value + mid :
            value = array[i]
            count += 1
    
    if count >= c :
        start = mid + 1
        result = mid
    else :
        end = mid - 1
        
print(result)
