# 못풀은 문제

Children = [[] for _ in range(300000)] # 연결 리스트
Cost = [[0,0] for _ in range(300000)] # 비용 dp 배열 (0 - 미참석) (1 - 참석)시 최소 비용

def traversal(sales,node) :
    Cost[node][0] = 0 # 참석하지 않았을 때 기본 적으로 0
    Cost[node][1] = sales[node] # 참석했을 때는 자기 비용으로 초기화

    # 리프 노드인 경우 순회가 끝난다.
    if not Children[node] :
        return

    # 리프노드가 아닌 경우 자식 노드를 순회
    for child in Children[node] :
        traversal(sales,child)

        extraCost = 1e9 # 자식 노드들이 모두 참석하지 않는 경우 가장 작은 값을 가져와야 한다.

        # 자식 노드에 대한 재귀호출이 끝나면 자기 자신을 갱신해준다.
        # 자식이 참석하는 경우와 참석 하지 않는 경우 중 더 작은 비용을 더해준다.
        if Cost[child][0] < Cost[child][1] : 
            Cost[node][0] += Cost[child][0]
            Cost[node][1] += Cost[child][0]
            extraCost = min(extraCost,Cost[child][1] - Cost[child][0]) # 자식을 참석시키기 위한 최소 추가 비용
        else :
            Cost[node][0] += Cost[child][1]
            Cost[node][1] += Cost[child][1]
            extraCost = 0 # 자식 중 한명이라도 참석한다면 추가 비용은 필요 없다. 

        Cost[node][0] += extraCost # 부모노드가 참석하지 않는 경우에 대하여 추가비용을 더해준다.



def solution(sales, links):
    
    # 입력받은 간선의 정보를 Children에 저장
    for link in links : 
        Children[link[0]-1].append(link[1]-1) 

    traversal(sales,0) # root 부터 순회

    return min(Cost[0][0],Cost[0][1])

print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17],[[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))