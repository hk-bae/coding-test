#https://programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
    
    answer = []
    states = [0] * (N+1) #현재 스테이지에 머무르는 사람의 수
    
    sum = 0
    
    for i in range(len(stages)) :
        index = stages[i]
        if index == (N+1) :# 모두 클리어한 경우
            sum += 1
        else :
            states[index] += 1
    
    
    for i in range(N, 0, -1) :
        sum += states[i]
        if sum == 0 :
            answer.append((i,0))
            continue
        else :
            failure = states[i] / sum
            answer.append((i,failure))
    
    answer.sort(key = lambda x : (-x[1],x[0]))
    
    result = []
    
    for stageNum,failure in answer :
        result.append(stageNum)
    
    return result


#이것이 취업을 위한 코딩테스트다 553pg
#내장함수를 사용하여 코드의 가독성은 높지만 시간은 조금 더 걸린다
def solution(N,stages) :
    answer = []
    length = len(stages)
    
    for i in range(1,N+1) :
        count = stages.count(i) #배열 내에서 i의 개수를 얻는 함수
        
        if length == 0 :
            fail = 0
        else :
            fail = count / length
        
        answer.append((i,fail))
        length -= count
        
    answer = sorted(answer,key=lambda t : t[1], reverse = True)
    
    answer = [i[0] for i in answer]
    return answer
