#이것이 취업을 위한 코딩테스트다 with 파이썬 558pg
#Amazon 인터뷰

def binary_search(array,start,end) :
  while start <= end:
    mid = (start+end) // 2
    if array[mid] == mid :
      return mid
    elif array[mid] > mid :
      end = mid - 1
    else :
      start = mid + 1

  return None

n = int(input())

data = list(map(int,input().split()))

fix_point = binary_search(data,0,n-1)

if fix_point == None :
  print(-1)
else :
  print(fix_point)
