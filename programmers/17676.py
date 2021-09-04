import re
from collections import deque

def timeToInterval(time) :
    time_list = re.split(':| |s',time) 
    # ms로 변환
    hour = int(float(time_list[1]) * 3600 * 1000)
    min = int(float(time_list[2]) * 60 * 1000)
    sec = int(float(time_list[3]) * 1000)
    t = int(float(time_list[4]) * 1000)
    
    
    end_time = (hour+min+sec) 
    start_time = (end_time - t + 1)
    return (start_time,end_time)
    

def solution(lines):

    
    timeLine = []
    n = 0

    for info in lines :
        start_time,end_time = timeToInterval(info) # 현재 구역의 시작, 끝 시간
        timeLine.append((start_time,end_time)) # 시작 지점
        n += 1
    
    
      
        
    max_value = 1
    
    for i in range(n) :
        cnt = 0
        tmp_s = timeLine[i][0]
        tmp_e = tmp_s + 999
        
        for j in range(n) :
            now_s = timeLine[j][0]
            now_e = timeLine[j][1]
            
            if tmp_s<=now_s<=tmp_e or tmp_s<=now_e<=tmp_e or (tmp_s > now_s and tmp_e < now_e) :
                cnt += 1
                
        max_value = max(cnt,max_value)
        
        cnt = 0
        tmp_s = timeLine[i][1]
        tmp_e = tmp_s + 999
        
        for j in range(n) :
            now_s = timeLine[j][0]
            now_e = timeLine[j][1]
            
            if tmp_s<=now_s<=tmp_e or tmp_s<=now_e<=tmp_e or (tmp_s > now_s and tmp_e < now_e) :
                cnt += 1
                
        max_value = max(cnt,max_value)
    
    return max_value


solution( [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
])