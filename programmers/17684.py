def solution(msg):
    
    dic = dict()
    answer = []
    # 1. 길이가 1인 모든 단어 초기화
    for i in range(26) :
        dic[chr(ord('A')+i)] = i+1
    
    index = 27 # 다음 저장할 인덱스
    
    n = len(msg)
    # 2. 문자열 확인
    i = 0
    while i < n :
        keys = dic.keys()
        w = msg[i]
        increment = 1
        for j in range(i+1,n) :
            if w + msg[j] in keys :
                w += msg[j]
                increment += 1
            else :
                answer.append(dic[w]) # 색인 번호 출력
                dic[w + msg[j]] = index
                index += 1
                break
        
        i += increment
        if i == n-1 :
            answer.append(dic[msg[i]])
            break
        elif i == n : # 마지막 단어가 되면
            answer.append(dic[w])
            break
            
    return answer