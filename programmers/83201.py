def get_grade(score) :
    if score  >= 90 :
        return "A"
    elif score >= 80 :
        return "B"
    elif score >= 70 :
        return "C"
    elif score >= 50 :
        return "D"
    else :
        return "F"
    
def solution(scores):
    answer = ""
    n = len(scores) # 학생 수
    for j in range(n) :
        max_scr = -1 
        min_scr = 101
        max_cnt = 0
        min_cnt = 0
        sum_value = 0
        avg_value = 0.0
        self_estimation = scores[j][j] # 자기 평가 점수
        for i in range(n):
            sum_value += scores[i][j]
            # 최고값 확인
            if scores[i][j] > max_scr :
                max_scr = scores[i][j]
                max_cnt = 1
            elif scores[i][j] == max_scr :
                max_cnt += 1 
            
            # 최저값 확인
            if scores[i][j] < min_scr :
                min_scr = scores[i][j]
                min_cnt = 1
            elif scores[i][j] == min_scr :
                min_cnt += 1 
        
        if self_estimation == max_scr and max_cnt == 1 :
            sum_value -= self_estimation
            avg_value = float(sum_value) / (n-1)
            # print("#1",avg_value)
        elif self_estimation == min_scr and min_cnt == 1 :
            sum_value -= self_estimation
            avg_value = float(sum_value) / (n-1)
            # print("#2",avg_value)
        else :
            avg_value = float(sum_value) / n
            # print("#3",avg_value)
        
        answer += get_grade(avg_value)
            
    return answer