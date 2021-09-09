def solution(files):
    answer = []
    new_files = []
    
    for i,file in enumerate(files) : 
        # 1. Head, Num, Tail 나누기
        file_lower = file.lower()
        print(file)
        head = ''
        num = ''
        num_len = 0
        
        now = 0 # 0 - head, 1 - num, 2 - tail
        for ch in file_lower :
            if now == 0 and (ch < '0' or ch > '9') :
                head += ch
            elif now == 0 : # 숫자 등장
                num += ch
                num_len += 1
                now = 1
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