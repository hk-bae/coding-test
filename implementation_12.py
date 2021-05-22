#이것이 취업을 위한 코딩테스트다 with 파이썬 525pg
#2020 카카오 신입 공채 문제
#https://programmers.co.kr/learn/courses/30/lessons/60061

#주어진 구조물이 가능한 구조물인지 확인하는 함수 
def isPossible(answer) :

    for x,y,stuff in answer :
        if stuff == 0 : # 기둥
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer : continue
            else : return False
            
        else : # 보
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer) : continue
            else : return False
    return True 



def solution(n, build_frame):
    answer = []
    
    #build_frame => (x,y,a,b)
    
    for build in build_frame : 
        tmp = [build[0],build[1],build[2]]
        if build[3] == 1 : #설치
            answer.append(tmp)
            if(not isPossible(answer)) :
                answer.remove(tmp)
        else : # 삭제
            answer.remove(tmp)
            if(not isPossible(answer)) :
                answer.append(tmp)
                
    answer.sort()
    return answer
