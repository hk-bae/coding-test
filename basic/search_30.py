#이것이 취업을 위한 코딩테스트다 pg 562
#https://programmers.co.kr/learn/courses/30/lessons/60060

from bisect import bisect_left, bisect_right

def count_by_range(array,left,right) :
    left_index = bisect_left(array,left)
    right_index = bisect_right(array,right)
    return right_index - left_index
    

array = [ [] for _ in range(10001)]
reversed_array = [ [] for _ in range(10001)]

def solution(words, queries):
    answer = []
    
    words_head = sorted(words) # 문자의 선행을 기준으로 정렬
    words_tail = [] # 문자의 후행을 기준으로 정렬
    for word in words :
        array[len(word)].append(word)
        reversed_array[len(word)].append("".join(reversed(word)))
    
    for i in range(10001) :
        array[i].sort()
        reversed_array[i].sort()
    
    for q in queries :
        if q[0] != '?':
            res = count_by_range(array[len(q)], q.replace('?','a'), q.replace('?','z'))
        else :
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?','a'), q[::-1].replace('?','z'))
        
        answer.append(res)

    return answer
