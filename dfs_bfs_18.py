# https://programmers.co.kr/learn/courses/30/lessons/60058

def check(p) :
    stack = []
    for ch in p :
        if ch == '(' :
            stack.append('(')
        else :
            if len(stack) > 0 : stack.pop()
            else : return False
    
    return True

def balance(p) :
    count_1 = 0
    count_2 = 0
        
    for i in range(len(p)) :
        if p[i] == '(' : count_1 += 1
        else : count_2 += 1
            
        if count_1 == count_2 :
            return i
    
def solution(p):
    
    #1
    if check(p) : return p
        
    #2
    index = balance(p)
    u = p[:index+1]
    v = p[index+1:]
        
    #3   
    if check(u) :
        return u + solution(v)
    #4
    else :
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1]) # u의 첫번째와 마지막을 제거
        for i in range(len(u)) :
            if u[i] == '(' : u[i] = ')'
            else : u[i] = '('
        
        answer += "".join(u)
    
    return answer
