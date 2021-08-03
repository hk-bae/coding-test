# 그래프 이론

-  아래 내용들을 기반으로 정리합니다.

- 이것이 취업을 위한 코딩테스트다 with 파이썬

- Introduction to the design and analysis of Algorithms, 3rd ed, Anany Levitin



1. [서로소 집합](#서로소-집합)
2. [크루스칼 알고리즘](#kruskal's-algorithm)
3. [위상정렬](#topological-sorting)



## 서로소 집합

* 공통 원소가 없는 두 집합

* 서로소 부분 집합들로 나눠진 원소들의 데이터를 처리하기 위한 자료구조

* Union-find 자료구조

  * union : 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
  * find : 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산

    

* 트리 자료구조를 이용하여 집합을 표현

* 알고리즘

  1. union(합집합) 연산을 확인하여, 서로 연결된 두 노드 A,B를 확인한다.
     1. A와 B의 루트 노드 A', B'을 각각 찾는다.
     2. A'을 B'의 부모 노드로 설정한다. (B'이 A'을 가리키도록 한다)
  2. 모든 union 연산을 처리할 때 까지 1번을 반복한다.

* 기본적인 서로소 집합 알고리즘 소스코드

  ````python
  # 특정 원소가 속한 집합을 찾기
  def find_parent(parent,x) :
    # 루트노드가 아니라면, 루트 노드를 찾을 때 까지 재귀적으로 호출
    if parent[x] != x :
      return find_parent(parent,parent[x])
    return parent[x]
  
  # 두 원소가 속한 집합을 합치기
  def union_parent(parent,a,b) :
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    
    if a < b :
      parent[b] = a
    else :
      parent[a] = b
      
  # 노드의 개수와 간선(union 연산)의 개수 입력 받기
  v,e = map(int,input().split())
  parent = [0] * (v+1) # 부모 테이블 초기화
  
  # 부모 테이블 상에서 부모를 자기 자신으로 초기화
  for i in range(1,v+1) :
    parent[i] = i
    
  #union 연산을 각각 수행
  for i in range(e) :
    a,b = map(int,input().split())
  	union_parent(parent,a,b)
  
  # 각 원소가 속한 집합 출력
  print('각 원소가 속한 집합: ',end = '')
  for i in range(1,v+1):
    print(find_parent(parent,i),end=' ')
  
  print()
  
  # 부모 테이블 내용 출력
  print('부모 테이블: ',end='')
  for i in range(1,v+1) :
    print(parent[i], end=' ')
  ````



* 이러한 서로소 집합은 사이클 판별에 사용된다.

  * 무방향 그래프 내에서의 사이클 판별
    * 방향 그래프에서의 사이클 여부는 DFS를 이용하여 판별할 수 있다.
  * 간선을 하나씩 확인하면서 두 노드가 포함되어 있는 집합을 합치는 과정으로 사이클 판별
    1. 각 간선을 확인하며 두 노드의 루트 노드를 확인한다.
       * 루트 노드가 서로 같다면 사이클이 발생한 것이다.
       * 루트노드가 서로 다르다면 두 노드에 대한 union 연산을 수행한다.
    2. 그래프에 포함된 모든 간선에 대하여 1번을 반복한다.

  ```python
  v,e = map(int,input().split())
  parent = [0] * (v+1)
  
  for i in range(1,v+1) :
    parent[i] = i
    
  # 사이클 발생 여부
  cycle = False
  
  for i in range(e) :
    a,b = map(int,input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent,a) == find_parent(parent,b):
      cycle = True
      break
    # 사이클이 발생하지 않았다면 union 수행
    else :
      union_parent(parent,a,b)
  
  ```

  

## Kruskal's Algorithm

### 최소 신장 트리

* 신장 트리는 그래프 알고리즘 문제로 자주 출제되는 문제유형이다.

  * 신장트리 : 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프

    * 이러한 조건은 트리의 성립 조건이기도 하다.

    ![스크린샷 2021-07-12 오후 7.26.21](/Users/baehangyeol/Library/Application Support/typora-user-images/스크린샷 2021-07-12 오후 7.26.21.png)

    * 최소 신장트리를 찾는 것이 문제로 나온다.



### 크루스칼 알고리즘 

* 그리디 알고리즘으로 분류 된다.
* 알고리즘
  1. 모든 간선을 오름차순으로 정렬
  2. **정렬된 간선을 하나씩 선택하되 사이클이 만들어지는 경우는 무시 **
     * 사이클이 발생하지 않는 간선에 대해서만 최소 신장 트리에 포함시킨다.
  3. 모든 간선에 대하여 2번의 과정을 반복한다.



* 구현

  * 시간 복잡도 O(ElogE)
  * 간선을 정렬하는 작업이 가장 오래 걸린다.
  * 크루스칼 내부에서 사용되는 서로소 집합 알고리즘의 시간 복잡도는 알고리즘의 시간 복잡도보다 작으므로 무시한다.

  ```python
  # 특정 원소가 속한 집합 찾기
  def find_parent(parent,x):
    # 루트 노드가 아니라면 루트 노드를 찾을 때 까지 재귀적으로 호출
    if parent[x] != x :
      return find_parent(parent,parent[x])
    return parent[x]
  
  # 두 원소가 속한 집합을 합치기
  def union_parent(parent,a,b) :
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
      parent[b] = a
     else :
      parent[a] = b
      
  # 노드의 개수와 간선의 개수 입력 받기
  v,e = map(int,input().split())
  parent = [0] * (v+1) # 부모 테이블 초기화
  
  # 모든 간선을 담을 리스트와 최종 비용을 담을 변수
  edges = []
  result = 0
  
  # 부모 테이블에서, 부모를 자기 자신으로 초기화
  for i in range(1,v+1) :
    parent[i] = i
    
  # 모든 간선에 대한 정보 입력 받기
  for _ in range(e) :
    a,b,cost = map(int,input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost,a,b))
    
  # 간선을 비용순으로 정렬
  edges.sort()
  
  # 간선을 하나씩 확인하며
  for edge in edges :
    cost,a,b = edge
    # 사이클이 발생하지 않은 경우에만 집합에 포함
    if find_parent(parent,a) != find_parent(parent,b) :
      union_parent(parent,a,b)
      result += cost
  
  print(result)
  ```

  

## Topological Sorting

* 방향 그래프의 모든 노드를 ' 방향성을 거스르지 않도록 순서대로 나열하는 것'
* 알고리즘
  1. 진입차수가 0인 노드를 큐에 넣는다.
  2. 큐가 빌 때 까지 다음의 과정을 반복한다.
     1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
     2. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
* 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 발생한 것이다.
* 위 과정에서 큐에서 빠져 나간 노드들을 순서대로 출력하면 위상 정렬을 수행한 결과가 된다.
* 위상절렬의 결과는 여러개 일 수 있다.



* 구현

  * 시간복잡도 O(V+E)
    * 모든 노드를 확인하면서, 해당 노드에서 출발하는 간선을 차례대로 제거

  ```python
  from collections import deque
  
  # 노드의 개수와 간선의 개수를 입력받기
  v,e = map(int,input().split())
  # 모든 노드에 대한 진입차수는 0으로 초기화
  indegree = [0] * (v+1)
  # 각 노드에 연결된 간선 정보를 담기 위한 연결리스트 초기화
  graph = [[] for _ in range(v+1)]
  
  # 방향 그래프의 모든 간선 정보 입력 받기
  for _ in range(e) :
    a,b = map(int,input().split())
    graph[a].append(b) # 정점 A에서 B로 이동 가능
    # 진입차수를 1 증가
    indegree[b] += 1
    
  # 위상 정렬 함수
  def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용
    
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
      if indegree[i] == 0 :
        q.append(i)
        
    # 큐가 빌 때까지 반복
    while q :
      # 큐에서 원소 꺼내기
      now = q.popleft()
      result.append(now)
      # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
      for i in graph[now] :
        indegree[i] -= 1
        # 새롭게 진입차수가 0이되는 노드를 큐에 삽입
        if indegree[i] == 0 :
          q.append(i)
  
    # 위상 정렬 수행 결과 출력
    for i in result :
      print(i,end = ' ')
        
  topology_sort()
   
  ```

  
