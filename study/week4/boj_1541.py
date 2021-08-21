
data = input().split('-')
res = 0

for i,s in enumerate(data) :
    num = sum(map(int,s.split('+')))
    if i == 0 :
        res += num
    else :
        res -= num

print(res)