# Shortest Path

-  아래 내용들을 기반으로 정리합니다.

- 이것이 취업을 위한 코딩테스트다 with 파이썬

- Introduction to the design and analysis of Algorithms, 3rd ed, Anany Levitin



## Overview

* 가장 짧은 경로를 찾는 알고리즘
* 네트워크에서 정점 u와 정점 v를 연결하는 경로 중에서 간선들의 가중치 합이 최소가 되는 경로
  * 간선의 가중치는 비용, 거리, 시간 등



* Single-source shortest paths problem

  * 주어진 정점을 시작으로 다른 정점에 이르는 가장 짧은 경로를 찾는 문제

  *  [다익스트라 알고리즘](#dijkstra-algorithm) , [벨만포드 알고리즘](#bellman-ford's-algorithm)

* All-pairs shortest paths problem

  * 그래프들의 모든 정점들 사이에 가장 짧은 경로를 찾는 문제
  * [플로이드 알고리즘](#floyd-warshall-algorithm)



## Dijkstra Algorithm

* 그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘
* 음의 가중치를 갖는 간선이 있는 경우 적용 불가
* 네트워크의 Link State Routing Protocol에 사용 ( OSPF 프로토콜 )
* 그리디 알고리즘의 일종
  * 매번 '가장 적은 비용이 적은 노드'를 선택해서 임의의 과정을 반복



* 알고리즘 원리

  1. 출발 노드를 선택

  2. 최단 거리 테이블 초기화 

     * 시작 노드는 0, 시작 노드에서 방문할 수 있는 노드는 해당 거리, 나머지는 무한대

  3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택

     * 선택된 노드를 방문 표시

  4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신

     * 계산된 거리와 기존 거리중 짧은 거리로 갱신

  5. 위 과정에서 3,4번 반복

     

* 시간 복잡도 

  * 인접 행렬 : O(|V|^2)
  * 인접 리스트 : O(|E|log|V|)



* 구현 1.

  * 여기서는 최단경로가 아닌 ''최단 거리'를 구하는 알고리즘으로 구현됨
  * 시간복잡도 : O(V^2)
  * 각 노드에 대한 최단 거리를 담는 1차원 리스트 선언
  * 단계마다 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 리스트의 모든 원소를 확인(순차 탐색)
  * input() 보다 더 빠르게 동작하는 sys.std.readline() 으로 치환함
  * 만약 노드의 개수가 **5,000개 이하** 라면 이 코드로 해결할 수 있다.
    * 노드 개수가 **10,000개**를 넘어가는 문제라면 이 코드로 해결하기 어렵다.

  ```python
  	import sys
    input = sys.std.readline
    INF = int(1e9) // 무한을 의미하는 값으로 10억 설정
    
    # n: 노드의 개수, m: 간선의 개수
    n,m = map(int,input().split())
    #시작 노드 번호
    start = int(input())
    #각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
    graph = [[] for i in range(n+1)]
    #방문한 적이 있는지 체크하는 목적의 리스트 만들기
    visited = [False] * (n+1)
    #최단거리 테이블 초기화
    distance = [INF] * (n+1)
    
    #모든 간선에 대한 정보 입력받기
    for _ in range(m) :
      #a에서 b로가는 비용이 c
      a,b,c = map(int, input().split())
      graph[a].append((b,c))
  
   # 방문하지 않은 노드들 중에서 최소 거리를 찾는 함수
   def get_smallest_node() :
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1,n+1):
      if distance[i] < min_value and not visited[i]:
        min_value = distance[i]
        index = i
    return index
  
  def dijkstra(start) :
    #시작 노드에 대해서 초기화
    distance[start] = 0
    vistied[start] = True
    for j in graph[start] :
      distance[j[0]] = j[1]
    
    # 시작 노드를 제외한 전체 n-1 개의 노드에 대해 반복
    for _ in range(n-1) :
      # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
      now = get_smallest_node()
      visited[now] = True
      
      # 현재 노드와 연결된 다른 노드를 확인
      for j in graph[now] :
        cost = distance[now] + j[1]
        # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 갱신
        if cost < distance[j[0]] :
          distance[j[0]] = cost
  
  # 다익스트라 알고리즘 수행
  dijkstra(start)
  
  # 모든 노드로 가기 위한 최단 거리 출력
  for i in range(1, n+1) :
    if distance[i] == INF :
      print("INFINITY")
    else :
      print(distance[i])
  
  ```

  

* 구현 2.

  * 시간복잡도 O(ElogV)
  * 이 코드는 자다 깨서도 작성할 수 있을 정도로 숙달되어야 함
  * 최단거리가 짧은 노드를 단순히 선형적으로 찾는 것을 개선
    * Heap 자료구조를 사용한다.
    * 특정 노드까지의 최단 거리에 대한 정보를 힙에 담아서 처리하므로 출발 노드로부터 가장 거리가 짧은 노드를 더욱 빠르게 찾을 수 있다.
    * 최소 힙 구조 기반 -> 파이썬의 우선순위 큐 라이브러리를 그대로 사용하면 된다.
      * 참고로 최대 힙을 사용하려면 우선순위에 음수 부호를 붙여서 넣어싿가 꺼낼 때 다시 음수 부호를 붙여서 원래의 값으로 돌려서 사용
      * 하나의 데이터를 삽입 및 삭제할 시의 시간 복잡도는 O(logN)

  ```python
  import heapq
  import sys
  input = sys.stdin.readline
  INF = int(1e9) # 무한을 의미하는 값으로 10억 설정
  
  # 노드의 개수, 간선의 개수를 입력 받기
  n,m = map(int,input().split())
  # 시작 노드 번호를 입력 받기
  start = int(input())
  # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
  graph = [[] for i in range(n+1)]
  # 최단거리 테이블을 모두 무한으로 초기화
  distance = [INF] * (n+1)
  
  # 모든 간선 정보 입력받기
  for _ in range(m) :
    #a번 노드에서 b번 노드로 가는 비용이 c
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    
  def dijkstra(start) :
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0 으로 설정하여 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q : # 큐가 비기 전까지 반복
      #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
      dist,now = heapq.heappop(q)
      #현재 노드가 이미 처리된 적이 있는 노드라면 무시
      if distance[now] < dist :
        continue
      # 현재 노드와 연결된 다른 인접한 노드들을 확인
      for i in graph[now] :
        cost = dist + i[1]
        if cost < distance[i[0]] :
          distance[i[0]] = cost
          heapq.heappush(q,(cost,i[0]))
  
  #다익스트라 알고리즘 수행
  dijkstra(start)
  
  # 모든 노드로 가기 위한 최단 거리 출력
  for i in range(n+1) :
    if distance[i] == INF :
      print("INFINITY")
    else :
      print(distance[i])
  
      
  ```
  


## Bellman Ford's Algorithm

* 음의 간선을 허용하는 최단 경로 알고리즘
* 다익스트라 알고리즘은 벨만 포드 알고리즘과 동일한 작업을 수행하고 속도도 빠르지만 가중치가 음수인 경우는 처리할 수 없다.
* 시간복잡도는 O(VE)
* 핵심 아이디어 
  * 중간에 최대 k개의 간선을 거쳐 정점 s로부터 정점 t에 이르는 최단 거리
    1. 시작 정점을 결정
    2. 시작 정점에서 다른 정점까지의 거리 값을 초기화
    3. 현재 정점에서 모든 인접 정점들을 탐색하며 기존에 저장된 인접 정점까지의 거리보다 현재 정점을 거쳐 인접 정점에 도달하는 경우가 더 짧은 경우 갱신
    4. 3번의 과정을 V-1 번 반복
    5. 위 과정을 모두 마치고 난 후 거리가 갱신되는 경우가 생긴다면 이는 음수 사이클이 존재하는 것

```python
import sys

input = sys.stdin.readline
INF = 1e9

def bellman_ford(start) :
    distance[start] = 0
    
    # 전체 n-1번 반복, 마지막 한번은 음수 싸이클 확인
    for i in range(n) :
        # 모든 간선 확인
        for j in range(m) :
            now = edges[j][0]
            next = edges[j][1]
            dist = edges[j][2]
            
            if distance[now] != INF and distance[next] > distance[now] + dist :
                distance[next] = distance[now] + dist
                # 음수 싸이클 판정
                if i == n-1 :
                    return False
    return True
                    

n,m = map(int,input().split())
distance = [INF] * (n+1)
edges = []

for _ in range(m) :
    a,b,c = map(int,input().split())
    edges.append((a,b,c))

if bellman_ford(1) :
    for i in range(2,n+1) :
        if distance[i] == INF :
            print('-1')
        else :
            print(distance[i])
else :
    print('-1')
```





## Floyd Warshall Algorithm

* 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우

* 다익스트라 알고리즘은 단계마다 최단 거리를 가지는 노드를 반복적으로 선택

* 플로이드 워셜 알고리즘 또한 단계마다 '거쳐 가는 노드'를 기준으로 알고리즘을 수행

  * 다만 매번 방문하지 않은 노드 중에서 최단 거리를 갖는 노드를 찾을 필요가 없다.
  * 현재 노드를 거쳐가는 모든 경로를 고려
  * 시간 복잡도는 O(N^3)

* 2차원 리스트에 최단 거리 정보를 저장

* 다익스트라 알고리즘은 그리디 알고리즘

  * 플로이드 워셜 알고리즘은 다이나믹 프로그래밍

* 구현

  ```python
  INF = int(1e9)
  
  # 노드의 개수 및 간선의 개수 입력
  n = int(input())
  m = int(input())
  #2차원 리스트(그래프) 만들고, 모든 값을 무한으로 초기화
  graph = [[INF] * (n+1) for _ in range(n+1)]
  
  # 자기 자신에서 자기 자신으로 가는 비용은 0 으로 초기화
  for a in range(1,n+1) :
    for b in range(1, n+1) :
      if a == b :
        graph[a][b] = 0
  
  # 각 간선에 대한 정보를 입력 받아 그 값으로 초기화
  for _ in range(m) :
    #a에서 b로 가는 비용 c
    a,b,c = map(int,input().split())
    graph[a][b] = c
    
  # 점화식에 따라 플로이드 워셜 알고리즘 수행
  for k in range(1,n+1) :
    for a in range(1, n+1):
      for b in range(1,n+1):
        graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
  
  # 수행된 결과를 출력
  for a in range(1,n+1) :
    for b in range(1,n+1):
      # 도달할 수 없는 경우
     if graph[a][b] = Inf:
      print("INFINITY", end= " ")
     else :
      print(graph[a][b], end= " ")
    print()
  ```

  