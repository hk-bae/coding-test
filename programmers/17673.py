def getPlayTime(start,end) :
    h1,m1 = start.split(":")
    h2,m2 = end.split(":")
    
    return (int(h2) - int(h1)) * 60 + int(m2)  - int(m1)
    

def solution(m, musicinfos):
    
    new_info = []
    m = m.replace('C#','1')
    m = m.replace('D#','2')
    m = m.replace('F#','3')
    m = m.replace('G#','4')
    m = m.replace('A#','5')
    
    k = 0 # 몇번째 입력 값인지 저장
    for info in musicinfos :
        
        info_list = list(info.split(","))
        
        info_list[3] = info_list[3].replace('C#','1')
        info_list[3] = info_list[3].replace('D#','2')
        info_list[3] = info_list[3].replace('F#','3')
        info_list[3] = info_list[3].replace('G#','4')
        info_list[3] = info_list[3].replace('A#','5')
        
        length = len(info_list[3]) # 음악 전체 길이
    
        play_time = getPlayTime(info_list[0],info_list[1]) # 재생 길이
        music = '' # 네오가 실제 들은 악보
        
        if play_time <= length :
            music = info_list[3][:play_time]
        else :
            q = (play_time // length)
            r = (play_time % length)    
            music = info_list[3] * q + info_list[3][:r]
        
        
        if m in music : # 네오가 들은 부분이 포함된 경우
            new_info.append((play_time,k,info_list[2]))
            k += 1
        
    
    new_info.sort(key = lambda x : (-x[0],x[1]))
    
    if new_info : answer = new_info[0][2]
    else : answer = "(None)"
    
    return answer