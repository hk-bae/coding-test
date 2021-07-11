# 이것이 코딩테스트다 pg 567
# https://www.acmicpc.net/problem/14501
n = int(input())
t = [] # 시간
p = [] # 페이
dp = [0] * (n+1) # dp[i] : i일부터 n일까지 낼 수 있는 최대 이익
max_value = 0

for _ in range(n) :
    x,y = map(int,input().split())
    t.append(x)
    p.append(y)

# dp[i] = max{ p[i] + dp[t[i] + i]}
# top-down 방식
for i in range(n-1,-1,-1) :
    time = t[i] + i #i일에 시작해서
    
    # 상담이 n일안에 끝날 수 있는 경우
    if time <= n :
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    else :
        dp[i] = max_value

print(max_value)

