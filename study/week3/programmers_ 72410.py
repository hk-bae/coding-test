def solution(new_id):
    
    recommend_id = ''
    k = 0 # 추천 아이디의 길이
    length = len(new_id)

    for i,c in enumerate(new_id) :
        if 'A' <= c <= 'Z' : # 1단계 : 대문자 -> 소문자
            recommend_id += c.lower()
            k += 1
        elif 'a' <= c <= 'z' or '0' <= c <= '9' or c == '-' or c == '_' : 
            recommend_id += c
            k += 1
        elif c == '.' : 
            if k == 0 or i == length-1 : # 4단계 : 처음 또는 마지막에 . 제거
                continue
            else : # 이전에 마침표가 있었으면 추가하지 않기
                if k > 0 and recommend_id[k-1] == '.' : # 3단계
                    continue
            recommend_id += c
            k += 1
        else : # 2단계 : 그 외 문자 제거
            continue

        if k == 15 : # 6단계 15자이면 stop
            if recommend_id[k-1] == '.' : # 마지막이 .이면 .도 자른다.
                recommend_id = recommend_id[:k-1]
                k -= 1
            break             

    if recommend_id == '' : # 빈문자열인 경우
        recommend_id = 'aaa' # 5단계
        k = 3    

    if recommend_id[-1] == '.' : # 4단계 : 마침표가 끝에 위치한다면 제거
        recommend_id = recommend_id[:-1]
        k -= 1

    if k < 3 : # 7단계 : 두 글자 이하인 경우 마지막 글자 반복
        while k < 3 :
            recommend_id += recommend_id[-1]
            k += 1

    return recommend_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))