import re
from bisect import bisect_left, bisect_right
import heapq

def solution(info, query):
    answer = []

    # languae,part,career,food,score
    data = [[[[[] for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(4)]
    
    strToIndex = {'-':0,'cpp':1,'java':2,'python':3,'backend':1,'frontend':2,'junior':1,'senior':2,'chicken':1,'pizza':2}

    # 각 info를 분류
    for string in info :
        language,part,carrer,food,score = string.split()
        l_i = strToIndex[language]
        p_i = strToIndex[part]
        c_i = strToIndex[carrer]
        f_i = strToIndex[food]
        data[l_i][p_i][c_i][f_i].append(int(score))
        data[0][p_i][c_i][f_i].append(int(score))
        data[l_i][0][c_i][f_i].append(int(score))
        data[l_i][p_i][0][f_i].append(int(score))
        data[l_i][p_i][c_i][0].append(int(score))
        data[0][0][c_i][f_i].append(int(score))
        data[0][p_i][0][f_i].append(int(score))
        data[0][p_i][c_i][0].append(int(score))
        data[l_i][0][0][f_i].append(int(score))
        data[l_i][0][c_i][0].append(int(score))
        data[l_i][p_i][0][0].append(int(score))
        data[l_i][0][0][0].append(int(score))
        data[0][p_i][0][0].append(int(score))
        data[0][0][c_i][0].append(int(score))
        data[0][0][0][f_i].append(int(score))
        data[0][0][0][0].append(int(score))

    for i in range(4) :
        for j in range(3) :
            for m in range(3) :
                for l in range(3) :
                    data[i][j][m][l].sort()
    

    # 각 쿼리마다 확인
    for string in query : 
        queryList = re.split(r" and | ",string)
        
        l_i = strToIndex[queryList[0]]
        p_i = strToIndex[queryList[1]]
        c_i = strToIndex[queryList[2]]
        f_i = strToIndex[queryList[3]]

        res = len(data[l_i][p_i][c_i][f_i]) - bisect_left(data[l_i][p_i][c_i][f_i],int(queryList[4]))      
        answer.append(res)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info,query))

