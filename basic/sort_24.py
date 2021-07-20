#https://www.acmicpc.net/problem/18310
n = int(input())
data = list(map(int,input().split()))

data.sort()
mid = len(data) // 2

print(data[mid-1])
