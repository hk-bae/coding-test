n,s,m = map(int,input().split())
data = list(map(int,input().split()))

d = [[0] * (m+1) for _ in range(n)]

if 0 <= s + data[0] <= m :
    d[0][s+data[0]] = 1

if 0 <= s - data[0] <= m :
    d[0][s-data[0]] = 1

for i in range(1,n) :
    for j in range(m+1) :
        if d[i-1][j] == 1 :
            plus = j + data[i]
            minus = j - data[i]
            if 0 <= plus <= m :
                d[i][plus] = 1
            if 0 <= minus <= m :
                d[i][minus] = 1

result = -1
for i in range(m+1) :
    if d[n-1][i] == 1 :
        result = i

                
print(result)