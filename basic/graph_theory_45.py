# 이것이 코딩테스트다 with 파이썬 590 pg
from collections import deque

# 테스트 케이스만큼 q반복
for tc in range(int(input())) :
  # 노드의 개수 입력 받기
  n = int(input())
  # 모든 노드에 대한 진입차수는 0으로 초기화
  indegree = [0] * (n+1)
  # 각 노드에 연결된 간선 정보를 담기 위한 인접 행렬 초기화
  graph = [[False] * (n+1) for _ in range(n+1)]
  # 작년 순위 정보를 입력
  data = list(map(int,input().split()))
  # 방향 그래프의 간선 정보 초기화
  for i in range(n) :
    for j in range(i+1,n) :
      graph[data[i]][data[j]] = True
      indegree[data[j]] += 1
  
  # 올해 변경된 순위 정보 입력
  m = int(input())
  for i in range(m) :
    a,b = map(int,input().split())
    # 간선의 방향 뒤집기
    if graph[a][b]:
      graph[a][b] = False
      graph[b][a] = True
      indegree[a] += 1
      indegree[b] -= 1
    else :
      graph[a][b] = True
      graph[b][a] = False
      indegree[a] -= 1
      indegree[b] += 1

  # 위상정렬 시작
  result = []
  q = deque()
  
  for i in range(1,n+1) :
    if indegree[i] == 0 :
      q.append(i)

  certain = True
  cycle = False

  for i in range(n) :
    # n개를 모두 위상정렬하기 전에 큐가 빈다면 사이클이 형성된 것
    if len(q) == 0 :
      cycle = True
      break
    
    # 큐의 원소가 2개 이상이라면 여러가지 정렬 결과가 발생
    if len(q) >= 2 :
      certain = False
      break

    # 큐에서 원소 꺼내기
    now = q.popleft()
    result.append(now)
    # 해당 원소와 관련된 노드들의 진입차수 1 감소
    for j in range(1,n+1) :
      if graph[now][j]:
        indegree[j] -= 1
        # 새롭게 진입차수가 0이되는 노드 삽입
        if indegree[j] == 0 :
          q.append(j)

  
  if cycle :
    print("IMPOSSIBLE")
  elif not certain :
    print("?")
  else:
    for i in result :
      print(i,end=' ')
    print()
