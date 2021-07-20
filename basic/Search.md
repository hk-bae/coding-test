# Search
- 아래 내용들을 기반으로 정리합니다.
- 이것이 취업을 위한 코딩테스트다 with 파이썬
- Introduction to the design and analysis of Algorithms, 3rd ed, Anany Levitin

## sequential search(순차 탐색)

- 완전탐색, Brute-force 알고리즘 기법
- c.f) dfs bfs 기법도 완전 탐색 기법이다.
- 리스트 안에 있는 특정 데이터를 찾기 위해 앞에서 부터 데이터를 하나씩 차례대로 확인하는 방법

- python code

        def sequential_search(n,target,array) :
            for i in range(n) :
                if array[i] == target :
                    return i + 1
    
- 시간복잡도 : O(N)


## binary search(이진 탐색)
- 정렬된 리스트에 대하여 탐색을 진행
- 데이터가 무작위일 경우는 사용할 수 없다.
- 이진 탐색은 탐색 범위를 절반씩 좁혀가며 데이터를 탐색한다.
- 시작점, 끝점, 중간점을 이용
- 찾으려는 데이터와 중간점 위치에 잇는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 게 이진 탐색 과정이다.
- 시간 복잡도 : O(logN)
- 재귀함수를 이용하여 구현할 수 있고 반복문을 이용하여 구현할 수 있다.

- python code

        # 재귀함수를 이용한 구현
          def binary_search(array,target,start,end):
            if start > end :
                return None
            mid = (start + end) // 2
            if array[mid] == target :
                return mid
            elif array[mid] > target :
                return binary_search(array,target,start,mid -1)
            else :
                return bianry_search(array,target,mid+1,end)
    
    
    ​    
        # 반복문을 이용한 구현
        def binary_search(array,target,start,end):
            while start <= end :
                mid = (start + end) // 2
                if array[mid] == target :
                    return mid
                elif array[mid] > target :
                    end = mid - 1
                else :
                    start = mid + 1
            
            return None
    
- 이진 탐색의 소스코드 구현을 할 줄 알아야 한다.
- 이진 탐색 문제는 탐색 범위가 큰 상황에서의 탐색을 가정하는 문제가 많다.
- 따라서 탐색 범위가 2,000만을 넘어가면 이진 탐색으로 문제 접근을 권한다.
- 이진 탐색 문제의 경우 데이터 입력 시간을 줄이기 위해 sys 라이브러리를 사용하는 것이 좋다.

        import sys
        
        input_data = sys.stdin.readline().rstrip()


## interpolation search (보간탐색)

- 이진 탐색과 유사한 방법
- 이진 탐색이 찾는 key 값을 항상 중앙 값과 비교 했다면, 보간 탐색은 key 값이 위치할 곳을 비례식으로 계산하여 비교하는 방안
- (list[high] - list[low]) : (k - list[low])  = (high - low) : (탐색위치 - low)

## binary search tree (BST ; 이진 탐색 트리)
- 탐색 작업을 효율적으로 하기 위한 자료구조
<img width="907" alt="스크린샷 2021-06-07 오후 3 53 40" src="https://user-images.githubusercontent.com/68215452/120972319-94cf9f80-c7a8-11eb-85ad-a2065faaf2a7.png">
- 왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드

