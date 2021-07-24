import copy
from bisect import bisect_left


n = int(input())
data = list(map(int,input().split()))
sorted_data =  set(copy.deepcopy(data))
sorted_data = list(sorted_data)
sorted_data.sort()

for i in data :
    print(bisect_left(sorted_data,i),end = ' ')