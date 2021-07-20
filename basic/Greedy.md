# Greedy Algorithm
- 아래 내용들을 기반으로 정리합니다.
- 이것이 취업을 위한 코딩테스트다 with 파이썬
- Introduction to the design and analysis of Algorithms, 3rd ed, Anany Levitin의 내용

## Definition
- **현재 상황에서 지금 당장 좋은 것만을 고르는 방법**을 의미한다.
- 최적화 문제(**optimization problem)** - 비용 이윤 경로 등 최대,최소 값을 찾는 문제
- 그리디 해법은 정당성 분석이 가장 중요하다.
- 항상 최적해가 아닐 수도 있다.
- 따라서 단순히 현재 상황에서 가장 좋아보이는 것(locally optimal)을 선택해도 최적의 해를 구할 수 있는지 검토
- 각 단계에서의 선택은 다음과 같은 특성을 만족해야 한다.

   >1. Feasible : 문제의 제약조건을 만족
   >2. Locally optimal : 그 step에서 찾을 수 있는 feasible choice들 중 가장 좋은 local choice여야 한다.
   >3. Irrevocable : 한 번 결정되면, 그 다음 step에서 바뀔 수 없다.

## Example

- 코딩테스트에서 대부분 그리디 문제는 **탐욕법으로 얻은 해가 최적의 해가 되는 상황에서 이를 추론**할 수 있어야 풀리도록 출제된다.
----
  ex) 거스름돈 문제
- 가장 큰 화폐 단위부터 돈을 거슬러 주는 것이 최적의 해를 보장하는 이유는?
- 가지고 있는 동전 중에 **큰 단위가 항상 작은 단위의 배수이므로 작은 단위를 종합해 다른 해가 나올 수 없다.**

----
그리디 알고리즘의 응용으로 다음이 있다. 자세한 내용들은 그래프 이론 등과 같은 파트에서 정리한다.
- Optimal Solutions
> MST(Minimal Spanning Tree), 
> Single-source shortest paths, 
> Simple Scheduling problems, 
> Huffman codes

- Approximations
> Traveling salesman problem, 
> Knapsack problem

