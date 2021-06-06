# 이것이 취업을 위한 코딩테스트다 with 파이썬 339pg
# https://www.acmicpc.net/problem/18352

from collections import deque

# n : 도시의 개수, m : 도로의 개수, k : 거리 정보, x : 출발 도시 번호
n,m,k,x = map(int,input().split()) 

#인접 리스트
a_list = [[] for _ in range(n+1)]

for _ in range(m) :
    start,end = map(int,input().split())
    a_list[start].append(end)
    

result = [-1] * (n+1) # 각 노드에 대하여 x로 부터 최단 거리
result[x] = 0

queue = deque()
queue.append(x) # 시작 노드 x
while queue :
    now = queue.popleft() 
    for a in a_list[now] : # 각 인접 노드에 대하여
        if result[a] == -1 : # 거리 계산이 안된 경우만
            result[a] = result[now] + 1 #자기 자신의 거리 + 1 을 넣어준다.
            if result[a] == k : continue
            else : queue.append(a)
                
                
check = False
for i in range(1,n+1) :
    if result[i] == k :
        print(i)
        check = True
    
if not check : print("-1")
