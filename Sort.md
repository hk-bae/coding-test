# Sort
- 아래 내용들을 기반으로 정리합니다.
- 이것이 취업을 위한 코딩테스트다 with 파이썬
- Introduction to the design and analysis of Algorithms, 3rd ed, Anany Levitin의 내용

## selection sort (선택정렬)
- 주어진 전체 리스트에서 *가장 작은 원소를 찾아서* 첫 번째 원소와 교환하는 방식

- python code

        def selection_sort(A) :
            n = len(A)
            for i in range(n-1) :
                min = i
                for j in range(i+1,n) :
                    if A[j] < A[min] : min = j
                    A[i],A[min] = A[min],A[i]

- 시간복잡도 : O(n^2)
- Brute-forece 알고리즘의 일종
- 선택정렬은 다른 알고리즘과 비교했을 때 비효율적이지만 데이터의 개수가 작은 경우에서는 나름대로 효율적이다.
- 코딩테스트에서는 특정 리스트에서 가장 작은 데이터를 찾는 일이 잦으므로 선택정렬 소스코드에 익숙해질 필요가 있다.


## bubble sort (버블정렬)
- *인근 2개의 원소*를 비교하여 리스트 전체를 정렬
- 리스트에 역순으로 데이터가 들어가 있는 경우 너무 많은 비교와 교환이 발생
- 인근 2개의 원소를 서로 비교해서 교환하는 동작을 반복하면 가장 큰 원소가 리스트의 가장 마지막 자리로 이동한다. "bubbling up"

- python code

        def bubble_sort(A) :
            n = len(A)
            for i in range(n-1) : # n-1번 반복
                for j in range(n -1 - i) : 
                    if A[j+1] < A[j] :
                        A[j+1],A[j] = A[j],A[j+1]
                        
- 시간복잡도 : O(n^2)
- Brute-forece 알고리즘의 일종

## insertion sort (삽입정렬)
- Decrease and Conquer
> 문제 사례를 동일한 의미의 더 작은 문제 사례로 줄여서 이해하는 것이 핵심 아이디어
> 더 작은 문제 사례를 해결
> 더 작은 문제 사례의 해결방법을 확장하여 원본 문제 사례의 알고리즘을 수립

- 삽입정렬은 decrease and conquer 알고리즘 기법을 이용
- A[0..n-1] 배열을 정렬하기 위해서 원소가 하나 적은 A[0..n-2] 배열을 정렬하는 것을 이용
- 이때 정렬된 배열 A[0..n-2]에 원소 A[n-1]을 적당한 위치에 삽입하는 것이 핵심 아이디어

- python code

        def insertion_sort(A) :
            n = len(A)
            for i in range(1,n) :
                target = A[i]
                j = i - 1
                while j>=0 and A[j] > target :
                    A[j+1] = A[j]
                    j = j - 1
                A[j+1] = target
                
        def insertion_sort_2(A) :
            n= len(A)
            for i in range(1,n) :
                for j in range(i,0,-1) : #인덱스 i부터 1까지 감소하며 반복하는 문법
                    if A[j] < A[j-1] : 
                        A[j],A[j-1] = A[j-1],A[j]
                    else :
                        break
                        
- 시간복잡도 : O(n^2)
- 삽입정렬의 시간 복잡도는  O(N^2) 이지만 최선의 경우 O(n)에 수렴한다. 
- 삽입정렬은 대상 리스트가 거의 정렬되어 있는 상태라면 매우 빠르게 동작한다.
- 따라서 거의 정렬되어 있는 상태로 입력이 주어지는 문제라면 퀵 정렬 등의 여타 정렬 알고리즘을 이용하는 것 보다 삽입 정렬을 이용하는 것이 정답 확률을 높일 수 있다.
- Best elementray sorting algorithm overall


## topological sorting (위상정렬)
- 전제 조건, 제약 조건이 있는 문제를 설계할 때 효율적인 방안
- DAG : Directed Acyclic Graph
- 간선이 일방향이고 사이클이 형성되지 않는 그래프를 시작정점에서 종료 정점까지 이르기 까지 순차적인 순서를 준수하며 정점을 정렬하는 방안

### DFS-based 알고리즘
- traversal stack에서 더이상 꺼낼 정점이 없을 때 까지 DFS 순회를 수행
- DFS 순회의 역순으로 위상 정렬 해결
- 만약 back edges가 있다면, 해당 그래프는 DAG가 아니며위상 정렬의 문제를 위한

<img width="1050" alt="topological_sort_dfs" src="https://user-images.githubusercontent.com/68215452/120886253-f0265400-c627-11eb-879f-2b1388d43cfe.png">

- 시간복잡도 : 인접 행렬 - O(V^2), 인접 리스트 - O(V +E)

### Source Reomval 알고리즘
- 그래프에 더 이상의 정점이 없을 때 까지 시작 정점을 반복적으로 제거, 시작 정점은 자신으로 진입하는 간선이 없는 정점을 의미
- 정점이 모두 제거되지 않았는데 시작 정점이 없다면, 해당 그래프는 DAG가 아니며 위상정렬의 필요조건을 위반
- 시간 복잡도는 DFS-based 알고리즘과 같다.

<img width="1056" alt="스크린샷 2021-06-05 오후 6 06 12" src="https://user-images.githubusercontent.com/68215452/120886424-d46f7d80-c628-11eb-947a-c79bf0ec19ba.png">



## merger sort (합병정렬)

- Divide and Conquer
> 가장 잘 알려진 알고리즘 설계 전략
> 1. 문제를 m개 (일반적으로 2개)의 부분으로 나눔
> 2. 작은 부분으로 나누어 재귀적으로 해결
> 3. 결과 값을 합쳐서 원본 문제의 해답을 구함

- merge sort에서 divide and conquer
1. 분할(divide) : 배열을 같은 크기의 2개의 부분 배열로 분할
2. 정복(conquer) : 부분 배열을 정렬. 부분 배열의 크기가 충분히 작지 않으면 재귀호출을 이용하여 다시 분할정복기법 이용 적용
3. 결




                
                
