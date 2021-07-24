import sys


input = sys.stdin.readline

n = int(input())

result = []
plus = [] # 양수
minus = [] # 음수, 0
zero = 0

for _ in range(n) :
    num = int(input())
    if num == 1 :
        result.append(1)
    elif num > 0 :
        plus.append(num)
    elif num < 0 :
        minus.append(num)
    else :
        zero += 1
        
plus.sort(reverse = True)

i = 0
length_plus = len(plus)

while (i+1) < length_plus :
    result.append(plus[i] * plus[i+1])
    i += 2
    
if i < length_plus :
    result.append(plus[i])
    

minus.sort()

k = 0
length_minus = len(minus)
while (k+1) < length_minus :
    result.append(minus[k] * minus[k+1])
    k += 2

if k < length_minus and zero == 0 :
    result.append(minus[k])
    
print(sum(result))

