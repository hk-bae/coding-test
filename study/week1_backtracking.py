# https://www.acmicpc.net/problem/1062
import sys

input = sys.stdin.readline

# 재귀호출을 이용한 백트래킹 수행
def learn(i,k) :
    global result
    
    if k == 0 : # k개의 단어를 모두 배운 경우
        cnt = 0 
        # 각 단어들에 대하여
        for word in data :
            cnt += 1
            for i in range(len(word)) :
                alp = word[i]
                if not learned[ord(alp) - ord('a')] : # 배우지 않은 단어가 있다면
                    cnt -= 1
                    break
        result = max(result,cnt)
        return
       
    for alp in range(i,26) :
        if not learned[alp] :
            learned[alp] = True
            learn(alp,k-1)
            learned[alp] = False

n,k = map(int,input().split())

data = [] # n개의 단어를 저장할 리스트

for _ in range(n) :
    word = input()
    data.append(word[4:len(word)-4]) # anta- , -tica 제거
    
# 배운 단어들
learned = [False] * 26
# 반드시 배워야하는 단어들
must = ['a','n','t','i','c'] 
for must_word in must :
    learned[ord(must_word)-ord('a')] = True 


result = 0
# 최소한의 a,n,t,i,c도 못배우는 경우
if k < 5 :
    print('0')
elif k == 26 : # 모든 알파벳을 다 배울 수 있는 경우
    print(n)
else :
    learn(0,k-5)
    print(result)   