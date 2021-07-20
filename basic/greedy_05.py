# 이것이 취업을 위한 코딩테스트다 314 pg
# 05. 볼링공 고르기

n,m = map(int,input().split())
balls = list(map(int,input().split()))

count = 0

for i in range(len(balls)) :
  for j in range(i+1,len(balls)) :
    if balls[i] is not balls[j] : count += 1

print(count)

# 모범 풀이 (512pg) => O(n) 으로 해결 가능

n,m = map(int, input().split())
data = list(map(int,input().split()))

# 1부처 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data :
  array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1,m+1):
  n -= array[i] #무게가 i인 볼링공의 개수 제외
  result += array[i] * n

print(result)
