from collections import deque

def solution(cacheSize, cities):
    time = 0
    
    n = len(cities) #  도시 크기
    
    size = 0
    in_memory = dict()
    queue = deque()
    
    for i in range(n):
        city = cities[i].lower()
        
        if city in in_memory.keys() : # 메모리 내에 존재
            time += 1 # cache hit!
            queue.append(city)
            in_memory[city] += 1
        else : # 메모리에 없음
            time += 5 # cache miss!
            in_memory[city] = 1
            queue.append(city)
            size += 1 
            if size > cacheSize : # 캐시 꽉참
                while size > cacheSize : 
                    target = queue.popleft()
                    if in_memory[target] == 1 :
                        in_memory.pop(target) # 제거
                        size -= 1
                    else :
                        in_memory[target] -= 1 # 1 감소
    
    return time


