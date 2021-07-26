import sys
from bisect import bisect_left

input = sys.stdin.readline


n = int(input())
data = list(map(int,input().split()))

data.sort()

value = 2e9
result = []

for i in range(n) :
    find = -data[i]
    index = bisect_left(data,find)
    
    if index + 1 < n and (index + 1) != i:
        if value > abs(data[index + 1] + data[i]) :
            value = abs(data[index + 1] + data[i])
            result = [data[i],data[index + 1]]
    if index < n and index != i:
        if value > abs(data[index] + data[i]) :
            value = abs(data[index] + data[i])
            result = [data[i],data[index]]
    
    if index - 1 >= 0 and (index - 1) != i:
        if value > abs(data[index - 1] + data[i]) :
            value = abs(data[index - 1] + data[i])
            result = [data[i],data[index - 1]]

    if value == 0 : break
        
if result[0] > result[1] :
    print(result[1],result[0])
else :
    print(result[0],result[1])