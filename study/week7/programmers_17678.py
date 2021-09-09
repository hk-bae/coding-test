def timeToMin(time) :
    
    hour,min = map(int,time.split(":"))
    min += hour * 60
    return min

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
    
    
from collections import deque
    
def solution(n, t, m, timetable):
    
    new_timetable = [] 
    
    for time in timetable :
        new_timetable.append(timeToMin(time)) # 분으로 변경하여 추가
    
    new_timetable.sort() # 시간 순 정렬
    q = deque(new_timetable) 
        
    ride = [0] * n # ride[k] : 9:00 + k * t 분에 탑승하는 사람 수 
    
    start = timeToMin('09:00')
    
    # 마지막 승객 전까지 크루 인원 태우기
    for i in range(n-1) : 
        bus_arrive = start + i * t
        while q :
            time = q.popleft() # 승객 도착 시간
            print("#1",time)
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
        print("#2",time)
        if time > last_bus : # 늦은 경우 무시
            break
        print(ride[n-1],m-1)
        if ride[n-1] == m-1 : # 마지막 한명 남음
            max_time = time - 1
            break
        
        ride[n-1] += 1
       
    return minToTime(max_time)