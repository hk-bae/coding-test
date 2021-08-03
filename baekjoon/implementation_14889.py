import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
people = [i for i in range(n)]

candidates = combinations(people,n//2)

result = 1e9



for start in candidates : # [1,3,5]
    team_start = 0
    for i in range(n//2-1) : 
        for j in range(i+1,n//2) :
            team_start += (data[start[i]][start[j]] + data[start[j]][start[i]])

    team_link = 0

    link  = list(set(people).difference(start))
    for i in range(n//2-1) :
        for j in range(i+1, n//2) :
            team_link += (data[link[i]][link[j]] + data[link[j]][link[i]])
        

    result = min(result,abs(team_start - team_link))
    
print(result)


for start in candidates : # [1,3,5]
    team_start = 0
    for i in range(n//2-1) : 
        for j in range(i+1,n//2) :
            team_start += (data[start[i]][start[j]] + data[start[j]][start[i]])

    team_link = 0

    link  = list(set(people).difference(start))
    for i in range(n//2-1) :
        for j in range(i+1, n//2) :
            team_link += (data[link[i]][link[j]] + data[link[j]][link[i]])
        

    result = min(result,abs(team_start - team_link))
    
print(result)
