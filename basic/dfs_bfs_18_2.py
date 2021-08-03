def isCorrectStr(p) :
    stack = []
    for c in p :
        if c == '(' :
            stack.append(c)
        else :
            if len(stack) == 0 :
                return False
            stack.pop()
    return True

def seperate(p) :
    
    left_side = 0
    right_side = 0
    
    seperate_index = 0
    
    for i in range(len(p)) :
        if p[i] == '(' :
            left_side += 1
        else :
            right_side += 1
            
        if left_side == right_side :
            seperate_index = i + 1
            break
    
    u = p[:seperate_index]
    v = p[seperate_index:]
    
    return (u,v)

def solution(p):
    # 빈문자열인 경우 그대로 반환
    if len(p) == 0 :
        return ''
    
    u,v = seperate(p)
    if isCorrectStr(u) :
        return u + solution(v)
    else :
        tmp = '(' + solution(v) + ')'
        u = u[1:-1]
        new_u = ''
        for c in u :
            if c == ')' :
                new_u += '('
            else :
                new_u += ')'
        tmp += new_u
        return tmp
