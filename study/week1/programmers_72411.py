# https://programmers.co.kr/learn/courses/30/lessons/72411
# implementation

from itertools import combinations

def solution(orders, course):
    answer = []
    # 각 메뉴들을 오름차순으로 정렬
    for i in range(len(orders)) :
        orders[i] = "".join(sorted(list(orders[i])))
    
    # 각 코스 별로 확인
    for k in course :
        # 모든 메뉴에 대해서 k개보다 크거나 같다면 조합
        candidate = dict()
        for menu in orders : 
            length = len(menu)
            # k개의 조합을 만들 수 없는 메뉴는 넘어간다.
            if length < k :
                continue
            # k개의 모든 조합
            tmp = combinations(list(menu),k)
            for item in tmp :
                word = "".join(item)  
                if word in candidate : # 후보에 이미 있다면
                    candidate[word] += 1
                else :
                    candidate[word] = 1
        # 모든 후보 값 중에서 2회 이상 나왔고 그 값이 가장 큰 것을 뽑는다.
        result = []
        max_value = 2
        for menu, cnt in candidate.items() :
            if cnt < 2 : continue
            if cnt > max_value :
                result = [menu]
                max_value = cnt
            elif cnt == max_value :
                result.append(menu)
                
        answer += result      
                    
    answer.sort()        
        
    return answer