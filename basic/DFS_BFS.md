# DFS BFS
- 아래 내용들을 기반으로 정리합니다.
- 이것이 취업을 위한 코딩테스트다 with 파이썬
- Introduction to the design and analysis of Algorithms, 3rd ed, Anany Levitin

## Intro
- 프로그래밍에서 그래프는 크게 2가지 방식으로 표현할 수 있다.
1. 인접 행렬 : 2차원 배열로 그래프의 연결 관계를 표현
- 연결된 노드 간의 거리를 원소로 넣는다.
- 연결되 지 않은 노드 간의 거리는 INF로 처리한다.

2. 인접 리스트 : 리스트로 그래프의 연결 관계를 표현
- 각 노드에 (연결된 노드, 거리) 를 저장한다.

- 이 두 방식은 시간과 공간의 비용에 대해 서로 상반된 이점을 갖는다.
- 인접 행렬은 모든 원소를 다 저장해야 하므로 메모리를 많이 필요한 반면에 특정 두 노드 간의 연결 관계에 대한 정보를 얻는 속도가 빠르다. (인덱싱)
- 인접 리스트는 연결된 정보만 저장하기 때문에 메모리를 효율적으로 사용하는 반면에 특정 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가 느리다. 

## DFS (Depth First Search)
-  깊이 우선 탐색, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
- 한 방향으로 갈 수 있을 때 까지 가다가 더이상 갈 수 없게 된다면 가장 가까운 갈림길로 돌아와서 이 곳으로 부터 다른 방향으로 탐색을 진행
- DFS는 스택 자료구조를 이용하며 구체적인 동작은 다음과 같다.
- 파이썬에서 스택구조는 단순히 list 자료형을 사용하면 된다.
-  stack = []
- stack.append(1)
- stack.pop()

1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.

2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.

3. 2번의 과정을 더이상 수행할 수 없을 때 까지 반복한다.

   

* 예제 코드

  ```python
  #DFS
  def dfs(graph,v,visited) :
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end= ' ')
    for i in graph[v] :
      if not visited[i] :
        dfs(graph,i,visited)
        
  # 각 노드가 연결된 정보를 리스트 자료형으로 표현
  graph = [ [],
           [2,3,8],
           [1,7],
           [1,4,5],
           [3,5],
           [3,4],
           [7],
           [2,6,8],
           [1,7]
          ]
  
  visited = [False] * 9
  
  dfs(graph,1,visited)
    
  ```

  


## BFS (Breadth First Search)
- 너비 우선 탐색, 가까운 노드 부터 탐색하는 알고리즘.
- BFS는 큐를 이용하며 구체적인 동작은 다음과 같다.
- 파이썬에서 큐 구조는 deque 라이브러리를 사용하는 것이 효율적이다.
- from collections import deque
- queue = deque()
- queue.append(5)
- queue.append(2)
- queue.popleft()
- queue.reverse() #역 순으로 바꾸기

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리 한다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
3. 2번의 과정을 더이상 수행할 수 없을 때 까지 반복한다.



* 예제코드

  ```python
  from collections import deque
    
  #BFS 메서드 정의
  def bfs(graph,start,visited) :
    #큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
      
    # 큐가 빌 때 까지 반복
    while queue :
      # 큐에서 하나의 원소를 뽑아 출력
      v = queue.popleft()
      print(v,end=' ')
      # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
      for i in graph[v] :
        if not visited[i] :
          queue.append(i)
          visited[i] = True
            
  # 각 노드가 연결된 정보를 리스트 자료형으로 표현
  graph = [ [],
           [2,3,8],
           [1,7],
           [1,4,5],
           [3,5],
           [3,4],
           [7],
           [2,6,8],
           [1,7]
          ]
  visited = [False] * 9
  
  bfs(graph,1,visited)
  ```

  
