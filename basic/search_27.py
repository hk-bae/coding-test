# 이것이 취업을 위한 코딩테스트다 367pg
# Zoho 인터뷰

def binary_search(array,target,start,end) :
    while start<=end :
      mid = (start + end) // 2
      if array[mid] == target :
        return mid
      elif array[mid] > target :
        end = mid - 1
      else :
        start = mid + 1
    return mid

n,target = map(int,input().split())

array = list(map(int,input().split()))

if array[binary_search(array,target,0,n-1)] != target  :
  print("-1")
else :
  low = binary_search(array,target-0.5,0,n-1)
  high = binary_search(array,target+0.5,0,n-1)
  if array[low] == target and array[high] == target :
    print(high - low + 1)
  elif array[low] == target or array[high] == target :
    print(high-low)
  else :
    print(high-low-1)


# pg 556 답안 예시 1

def count_by_value(array,x) :
    n = len(array)
    
    a = first(array,x,0,n-1)
    
    if a == None :
        return 0
    
    b = last(array,x,0,n-1)
    
    return b - a + 1
    
def first(array,target,start,end) :
    if start > end :
        return None
    
    mid = (start + end) // 2
    
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target :
        return mid
    elif array[mid] >= target :
        return first(array,target,start,mid - 1)
    else :
        return first(array,target,mid + 1,end)

def last(array,target,start,end) :
    if start > end :
        return None
    mid = (start + end) // 2
    
    if(mid == n -1 or target < array[mid + 1]) and target == array[mid] :
        return mid
    elif array[mid] > target :
        return last(array,target,start,mid - 1)
    else :
        return last(array,target,mid +1,end)

n,x = map(int,input().split())
array = list(map(int,input().split())

count = count_by_value(array,x)

if count == 0 :
    print(-1)
else :
    print(count)

# pg 557 답안예시 2
# 파이썬의 이진 탐색 라이브러리 bisect 활용

from bisect import bisect_left, bisect_right

#값이 [left_value,right_value]인 데이터의 개수를 반환하는 함수

def count_by_range(array,left_value,right_value) :
    right_index = bisect_right(array,right_value)
    left_index = bisect_left(array,left_value)
    
    return right_index - left_index

#이하 생략

