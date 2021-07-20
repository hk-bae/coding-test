#https://programmers.co.kr/learn/courses/30/lessons/60057
#문자열 압축
def solution(s):

    optimal = 0 #최적 압축 길이
    length = 1 #pattern 길이
    start_i = 0 #패턴 시작 인덱스
    end_i = start_i + length #패턴 끝 인덱스
    previous_pattern = "" #이전 패턴
    count = 1 
    compression = 0 # 압축된 길이
    
    while True :
        pattern = s[start_i:end_i] #패턴 확인
        #패턴이 일치할 경우
        if previous_pattern == pattern :
            count += 1
            compression += length # pattern 길이만큼 압축됨
        else : #불일치할 경우 이전에 성립된 패턴이 있으면 그 숫자의 길이만큼 늘어남
            if count != 1 : 
                compression -= len(str(count))
                count = 1
        
        previous_pattern = pattern #현재 패턴을 이전 패턴으로 저장
        start_i = end_i 
        end_i = start_i + length
        
        # 패턴이 끝까지 도달했을 때
        if end_i > len(s) : 
            if count != 1 : 
                compression -= len(str(count))
                count = 1
            if optimal < compression : 
                optimal = compression #현재까지 최적보다 많이 압축되었으면 optimal 변경
            
            length += 1 #다음 패턴 길이 설정
            #패턴 길이가 전체 길이의 절반보다 크다면 더 볼 필요가 없음.
            if length > len(s) // 2  : break  
            start_i = 0 
            end_i = start_i + length
            compression = 0
            previous_pattern = ""
    
    return len(s) - optimal
