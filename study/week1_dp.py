# https://programmers.co.kr/learn/courses/30/lessons/72414

def timeToIndex(time) :
    h,m,s = map(int,time.split(':'))
    return 3600 * h + 60 * m + s

def indexToTime(index) :
    
    h = index // 3600
    h = '0' + str(h) if h < 10 else str(h)
        
    index = index % 3600
    m = index // 60
    m = '0' + str(m) if m < 10 else str(m)
        
    s = index % 60
    s = '0' + str(s) if s < 10 else str(s)
        
    return h+":"+m+":"+s

def solution(play_time, adv_time, logs):
    answer = ''
    play_time = timeToIndex(play_time) # 시간 -> 초(인덱스)
    adv_time = timeToIndex(adv_time) # 시간 -> 초(인덱스)
    dp = [0] * (play_time + 1) # 해당 시간의 누적 시청자 수를 저장할 배열
    
    for log in logs :
        start,end = log.split('-')
        start = timeToIndex(start)
        end = timeToIndex(end)
        dp[start] += 1 # 시작 시간 기록
        dp[end] -= 1 # 종료 시간 기록
        
    # 구간 별 시청자 기록
    for i in range(1,play_time+1) :
        dp[i] += dp[i-1] 
    
    # 구간 별 누적 시청자 기록
    for i in range(1,play_time + 1) :
        dp[i] += dp[i-1]

    most_view = 0                           # 5
    max_time = 0                          
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < dp[i] - dp[i - adv_time]:
                most_view = dp[i] - dp[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < dp[i]:
                most_view = dp[i]
                max_time = i - adv_time + 1
        
    answer = indexToTime(max_time)
    
    return answer