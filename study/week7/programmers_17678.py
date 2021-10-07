# 셔틀 버스
from collections import deque

# 시간 문자열을 분(int)으로 변환하는 함수
def timeToMin(time) :  
    hour,min = map(int,time.split(":"))
    min += hour * 60
    return min

# 분(int)를 시간 문자열로 변환하는 함수
def minToTime(min) :
    hour = min // 60
    min = min - 60 * hour
    time = ''
    if hour < 10 : 
        time += ('0'+str(hour))
    else :
        time += str(hour)
        
    time += ':'
    
    if min < 10 :
        time += ('0' + str(min))
    else :
        time += str(min)

    return time 
        
def solution(n, t, m, timetable):

    # 기존 타임테이블을 분(int)로 담기위한 배열
    new_timetable = []  
    
    for time in timetable :
        new_timetable.append(timeToMin(time)) # 분으로 변경하여 추가
    
    new_timetable.sort() # 시간 순 정렬

    # 각 승객의 도착 시간을 큐에 담는다.
    q = deque(new_timetable)

    # 각 배차마다 탑승하는 사람의 수
    # ride[k] : 9:00 + k * t(배차간격) 분에 탑승하는 사람 수      
    ride = [0] * n 
    
    start = timeToMin('09:00') 
    
    # 마지막 셔틀 전까지 크루 인원 태우기
    for i in range(n-1) : 
        bus_arrive = start + i * t # 버스 도착시간
        while q :
            time = q.popleft() # 승객 도착 시간
            if time > bus_arrive : # 늦은 경우
                q.appendleft(time)
                break
                
            if ride[i] == m : # 정원 초과
                q.appendleft(time)
                break

            ride[i] += 1 # 탑승
    
    
    # 마지막 셔틀 버스를 탈 수 있는 최대 시간 구하기
    last_bus = start + (n-1) * t # 마지막 버스 시간
    max_time = last_bus
    
    while q :
        time = q.popleft() # 승객 도착 시간
        
        # 남은 승객들이 모두 늦은 경우
        if time > last_bus : 
            break
        
        # 마지막 한명 남음
        if ride[n-1] == m-1 : 
            max_time = time - 1
            break
        
        ride[n-1] += 1
       
    return minToTime(max_time)