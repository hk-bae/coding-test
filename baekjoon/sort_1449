n,l = map(int,input().split())
data = list(map(int,input().split()))

data.sort()

cnt = 1
tmp = data[0] + l - 1

for i in range(1,n) :
    if tmp < data[i] :
        cnt += 1
        tmp = data[i] + l - 1

print(cnt)