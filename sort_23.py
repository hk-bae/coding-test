#https://www.acmicpc.net/problem/10825

n = int(input())

l = []

for _ in range(n) :
    data = list(input().split())
    l.append((data[0],int(data[1]),int(data[2]),int(data[3])))

l.sort(key = lambda data : (-data[1],data[2],-data[3],data[0]))

for i in range(n) :
    print(l[i][0])
