import sys

input = sys.stdin.readline

stack1 = list(input().rstrip()) # stack1의 top이 커서 위치 유지
stack2 = []

m = int(input())
for _ in range(m) :
    command = list(input().rstrip())

    if command[0] == 'L' : # 왼쪽
        if stack1 : 
            stack2.append(stack1.pop())
            
    elif command[0] == 'D' : # 오른쪽
        if stack2 :
            stack1.append(stack2.pop())
            
    elif command[0] == 'B' : # 삭제
        if stack1 :
            stack1.pop()    
    else : # 삽입
        ch = command[2]
        stack1.append(ch)
        
print(''.join(stack1 + list(reversed(stack2))))