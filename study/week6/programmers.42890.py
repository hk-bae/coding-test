from itertools import combinations

def solution(relation):
    answer = 0
    
    row = len(relation) # 테이블 행 개수
    col = len(relation[0]) # 테이블 열의 개수

    data = [ index for index in range(col)]  # 모든 칼럼

    candidate_keys = [] # 후보키 조합 {i1,i2,i3..,in}
    
    # k개를 뽑는 조합을 고려 (1 ~ col)
    for k in range(1,col+1) :
        candidate = list(combinations(data,k)) 
        
        for indexs in candidate : # 각 인덱스 조합에 대하여
            uniqueness = True
            minimality = True
            tmp_dict = dict() # 만족하는 키 모음
            # 최소성 확인
            for key in candidate_keys :
                if key & set(indexs) == key :
                    minimality = False
                    break
                    
            if not minimality :
                continue
            
            # 유일성 확인
            for row in relation : 
                tmp = ""
                
                for i in range(k) :
                    tmp += row[indexs[i]] #각 열의 값을 이어 붙인다
                    
                if tmp in tmp_dict.keys() : # 중복이 있으면 유일성 만족 못함
                    uniqueness = False
                    break
                else :
                    tmp_dict[tmp] = True
                    
                if not uniqueness :
                    break
        
            if uniqueness : 
                candidate_keys.append(set(indexs))
                answer += 1
                     
        
    return answer