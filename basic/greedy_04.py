n = int(input()) # 1<= n <= 1000
coins = list(map(int,input().split()))

coins.sort()

target = 1 

for coin in coins : 
  if target < coin :
    break
  target += coin

print(target)
