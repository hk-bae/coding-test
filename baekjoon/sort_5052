import sys

def check(data) :
    previous = data[0]
    
    for i in range(1,len(data)) :
        if data[i].startswith(previous) :
            return False
        previous = data[i]
        
    return True

input = sys.stdin.readline

t = int(input())
result = []

for _ in range(t) :
    n = int(input())
    data = []
    for _ in range(n) :
        data.append(input().rstrip())
    
    data.sort()
    result.append(check(data))
        
for check in result :
    if check :
        print("YES")
    else :
        print("NO")
