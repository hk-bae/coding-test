#럭키 스트레이트
#https://www.acmicpc.net/problem/18406

def lucky_straight(rating) : 
    half_len = int(len(rating) / 2)
    head_sum = sum(map(int,rating[0:half_len])) #앞부분 합
    tail_sum = sum(map(int,rating[half_len:len(rating)])) #뒷부분 합
    if head_sum == tail_sum : print("LUCKY")
    else : print("READY")    

#시작
rating = input()
lucky_straight(rating)
