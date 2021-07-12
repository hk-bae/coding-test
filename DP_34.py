#https://www.acmicpc.net/problem/18353

n = int(input())
data = list(map(int,input().split()))

# d[i] : data[i]를 마지막으로 하는 부분수열의 최대 길이
d = [1] * n

for i in range(1,n) :
    for j in range(0,i) :
        if data[j] > data[i] :
            d[i] = max(d[i], d[j] + 1)
            
print(n - max(d))


