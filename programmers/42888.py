def engToKor(term) :
    if term == "Enter" :
        return "님이 들어왔습니다."
    elif term == "Leave" :
        return "님이 나갔습니다."
    else :
        return "Change" 

def solution(record):
    answer = []
    
    user = dict()

    for string in record :         
        data = string.split()
        if data[0] != "Leave" :
            user[data[1]] = data[2]
    
    for string in record :
        data = string.split()
        if data[0] != "Change" :
            answer.append(user[data[1]]+engToKor(data[0]))
        
        
    return answer
    
r = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
