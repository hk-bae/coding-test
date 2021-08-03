# https://www.acmicpc.net/problem/1517

import sys

result = 0

input = sys.stdin.readline
def merge_sort(start,end) :
    global result
  
    n = end - start
    if n > 1 :
        mid = (start+end) // 2
        merge_sort(start,mid)
        merge_sort(mid,end)

        new_arr = []
        i,j = start,mid
        tmp = 0
        while i < mid and j < end :
            if array[i] <= array[j] :
                new_arr.append(array[i])
                i += 1
                result += tmp # swap 횟수 추가
            else : 
                new_arr.append(array[j])
                j += 1
                tmp += 1 # 왼쪽 배열보다 우선으로 들어간 수를 카운트
                
        if i == mid :
          for k in range(j,end) :
            new_arr.append(array[k])
        else : 
          for k in range(i,mid) :
            new_arr.append(array[k])
            result += tmp # 남은 swap 횟수 추가
            
        for i in range(start,end) :
            array[i] = new_arr[i-start]
            
n = int(input())
array = list(map(int,input().split()))
merge_sort(0,n)

print(result)