# 파일명 정렬

def solution(files):
    answer = []
    new_files = []

    # 1. Head, Num, Tail 나누기
    for i,file in enumerate(files) :     
        
        file_lower = file.lower()
        
        head = ''
        num = ''
        num_len = 0 # 1~5 범위만 가능
        now = 0 # 0 - head, 1 - num, 2 - tail

        for ch in file_lower :
            # 아직 Head 부분이면서 숫자가 아닌 경우
            if now == 0 and (ch < '0' or ch > '9') :
                head += ch
            elif now == 0 : # 숫자 등장
                num += ch
                num_len += 1
                now = 1
            # Number 부분이면서 5글자 이하
            elif now == 1 and num_len < 5 and ('0'<=ch<='9') : 
                num_len += 1
                num += ch
            elif now == 1 and (num_len >= 5 or (ch < '0' or ch > '9')) :
                break
            
                
        # 2. (HEAD,NUM,i,파일명) 순으로 new_files에 추가
        new_files.append((head,int(num),i,file))
        
    # 3. 파일 정렬
    new_files.sort()
    
    # 4. answer에 옮기기
    for _,_,_,file in new_files :
        answer.append(file)
        
    return answer