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
3. 결합(combine) : 정렬된 부분배열을 다음과 같이 하나의 배열에 통합
> 부분배열의 각각 첫 번째 원소의 크기 비교
> 더 작은 원소를 통합된 배열 공간에 옮김
> 옮겨진 부분배열의 다음 원소를 다른 부분배열의 원소와 비교
> 위의 과정을 부분배열 중 하나가 빌 때까지 반복
> 원소가 남은 부분배열은 남은 원소들을 통합한 배열의 다음 부분에 차례로 복사

- python code
        
        import copy

        def merge_sort(a) :
            n = len(a)
            b = []
            c = []

            if n > 1 :
                # divde
                middle = n // 2
                b[0:middle] = copy.deepcopy(a[0:middle]) 
                c[0:middle] = copy.deepcopy(a[middle:])
                merge_sort(b)
                merge_sort(c)
                # conquer
                merge(b,c,a)
                
        def merge(b,c,a) :
            p = len(b)
            q = len(c)
                    
            i,j,k = 0,0,0
                    
            #정렬된 b와 c배열을 비교해 가며 작은 것 부터 차례로 a에 삽입
            while i<p and j<q :
                if b[i] <= c[j] :
                    a[k] = b[i]
                    i = i + 1
                else :
                    a[k] = c[j]
                    j = j + 1
                k = k + 1
                        
            # 남은 부분 카피
            if i == p :
                a[k:] = copy.deepcopy(c[j:])
            else :
                a[k:] = copy.deepcopy(b[i:])




        a = [1,4,5,6,2,4,6,8,0,1,29,3]

        merge_sort(a)

        print(a)
        
- 시간복잡도 : O(nlogn)

### quicksort (퀵 정렬)

1. 기준값 선택 (pivot : partitioning element) : 일반적으로 첫 번째 원소
2. 피봇보다 작은 원소들은 왼쪽으로 큰 원소들은 오른으로 분류한 후 그 사이에 피봇을 이동시킴
3. 이때 피봇의 위치는 정렬된 최종 위치이며, 피봇을 기준으로 배열은 불균등하게 양분됨
4. 각각의 부분 배열을 위의 과정을 재귀적으로 반복하여 정렬

- 사용되는 알고리즘 : Hoare's partitioning
> 피봇 : 가장 왼쪽 숫자라고 가정
> 두 개의 변수 low와 high를 사용
> low는 피봇보다 작으면 통과, 크면 정지
> high는 피벗보다 크면 통과, 작으면 정지
> 정지된 위치의 숫자를 교환
> low와 high가 교차하면 종료

<img width="1056" alt="스크린샷 2021-06-05 오후 6 06 12" src="https://user-images.githubusercontent.com/68215452/120913541-b9f1de80-c6d2-11eb-81b6-6f413fedd397.png">


- python code

        def quick_sort(array,start,end) :
            if start >= end : # 원소의 개수가 1개인 경우 종료
                return
            pivot = start # 첫번째 원소를 피봇으로 설정
            left = start + 1
            right = end
            
            while left <= right :
                # 피벗보다 큰 데이터를 찾을 때 까지 반복
                while left <= end and array[left] <= array[pivot] :
                    left += 1
                
                # 피벗보다 작은 데이터를 찾을 때 까지 반복
                whilr right > start and array[right] >= array[pivot] :
                    right -= 1
                
                if left > right : #엇갈렸다면 작은 데이터와 피벗을 교체
                    array[right],array[pivot] = array[right] >= array[pivot]
                else :
                array[left],array[right] = array[right],array[left]
                
            # 분할 이후 왼쪽과 오른쪽에 대하여 퀵정렬 재귀 호출
            quick_sort(array,start,right - 1)
            quick_sort(array,right + 1, end)
            
            
            #파이썬의 장점을 살려 짧게 작성한 퀵 정렬 소스코드
            #피벗과 데이터를 비교하는 비교 연산횟수가 증가하므로 시간 면에서는 비효율적
            def quick_sort2(array) :
                if len(array) <= 1 :
                    return array
                
                pivot = array[0] # 피벗은 첫 번째 원소
                tail = array[1:] #피벗을 제외한 리스트
                
                left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
                right_side = [x for x in tail if x > pivot] #분할된 오른쪽 부분
                
                #분할 이후 왼쪽과 오른쪽 부분에 대한 각각 정렬을 수행하고 전체 리스트 반환
                return quick_sort2(left_side) + [pivot] + quick_sort(right_side)
                
- 시간 복잡도 : Best Case(O(nlogn)), Worst Case(O(n^2)), Average case(O(nlogn))
- 퀵정렬은 호어 파티셔닝 기법을 사용할 때 이미 데이터가 정렬되어 있는 경우에는 매우 느리게 동작한다. (삽입정렬과 반대)
        

### 계수정렬(count sort)

- Space for Time Trade-Offs
> 문제를 더 쉽게 해결하기 위해 미리 입력 데이터를 처리해서 별도의 저장 공간에 유용한 정보를 저장해두는 전략

- 카운트 정보를 배열을 정렬하는데 사용한다.
- 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘    
- 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용 가능
- 일반적으로 가장 큰 데이터와 작은 데이터의 차이가 1,000,000을 넘지 않을 때

- python code

        def count_sort(array) :
            #모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
            count = [0] * (max(array)+1)
            
            result = []
            
            # 각 데이터에 해당하는 인덱스 값 증가
            for i in range(len(array)) :
                count[array[i]] += 1
                
            for i in range(len(count)) :
                for j in range(count[i]) :
                    result.append(i)
                    
            return result
            
- 모든 데이터가 양의 정수인 상황에서 데이터의 개수를 N, 데이터 중 최대 값의 크기를 K라고 할 때, 계수 정렬의 시간 복잡도는 O(N+K) 이다.
- 사실상 현존하는 정렬 알고리즘 중에서 기수 정렬과 더불어 가장 빠르다.
- 하지만 공간 효율성에 심각한 비효율성을 초래할 수 있다.
- 동일한 값을 가지는 데이터가 여러 개 등장할 때 적합하다.
- 데이터의 특성을 파악하기 어렵다면 퀵 정렬을 이용하는 것이 유리하다.


### heap sort (힙 정렬)

### 파이썬의 정렬 라이브러리
- 알고리즘 문제를 다룰 때 앞서 다루었던 정렬 알고리즘을 직접 작성하게 되는 경우도 있지만 미리 만들어진 라이브러리를 이용하는 것이 효과적인 경우가 더 많다.

- sorted()는 집합 자료형, 딕셔너리 자료형 등을 입력받아서 리스트 자료형 결과를 반환한다.
- 리스트 변수가 하나 있을 때는 리스트 객체의 내장 함수인 sort()를 이용할 수 있다.
- sort()나 sorted()를 이용할 때에는 key 매개변수를 입력받을 수 있다.
- key 값으로는 *하나의 함수*가 들어가야 하며 이는 정렬 기준이 된다.

- sorted() 는 퀵 정렬과 동작 방식이 비슷한 병합 정렬을 기반으로 구현됨.
- 병합정렬은 일반적으로 퀵 정렬보다 느리지만 최악의 경우에도 *시간 복잡도 O(NlogN)* 을 보장
- 따라서 문제에서 별도의 요구가 없다면 기본 정렬 라이브러리를 사용하고, 데이터의 범위가 한정되어 있으며 더 빠르게 동작해야 할 때는 계수 정렬을 사용하는 것이 좋다.

- 코딩 테스트에서 정렬 알고리즘이 사용되는 문제 유형
1. 정렬 라이브러리로 풀 수 있는 문제
2. 정렬 알고리즘의 원리에 대해서 물어보는 문제
3. 더 빠른 정렬이 필요한 문제
