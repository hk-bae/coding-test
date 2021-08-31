from collections import deque
import sys
sys.setrecursionlimit(10**5)

class Node :
    def __init__(self,data,left_node,right_node) :
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
        

def preorder(node) :
    global preorder_list, tree
    preorder_list.append(node)
    if tree[node].left_node != None :
        preorder(tree[node].left_node)
    if tree[node].right_node != None :
        preorder(tree[node].right_node)

def postorder(node) :
    global postorder_list
    if tree[node].left_node != None :
        postorder(tree[node].left_node)    
    if tree[node].right_node != None :
        postorder(tree[node].right_node)
    postorder_list.append(node)

# 삽입할 데이터, 부모의 노드 번호
def binary_search(data,parent) :
    global tree
    
    parent_data = tree[parent].data # 부모 노드의 데이터
    if parent_data > data :
        if tree[parent].left_node == None :
            return (parent,True)
        else :
            return binary_search(data,tree[parent].left_node) # 왼쪽 서브트리 탐색
    else : 
        if tree[parent].right_node == None :
            return (parent,False)
        else : 
            return binary_search(data,tree[parent].right_node) # 오른쪽 서브트리 탐색
    
    
        

def solution(nodeinfo):
    global preorder_list,postorder_list,tree
    
    preorder_list = [] 
    postorder_list = []
    
    new_nodeinfo = []
    tree = {} # 각 노드를 담을 딕셔너리
    
    # 각 노드에 노드 번호 저장
    for i in range(len(nodeinfo)) : 
        new_nodeinfo.append((nodeinfo[i][0],nodeinfo[i][1],i+1))
        tree[i+1] = Node(nodeinfo[i][0],None,None)
    
    # y 내림차순 정렬
    new_nodeinfo.sort(key = lambda p : (-p[1],p[0]))
    
    for i in range(1,len(new_nodeinfo)) : 
        
        parent,isLeft = binary_search(new_nodeinfo[i][0],new_nodeinfo[0][2]) # 현재 노드가 들어갈 위치 탐색

        if isLeft : 
            tree[parent].left_node = new_nodeinfo[i][2]
        else :
            tree[parent].right_node = new_nodeinfo[i][2]
            
    preorder(new_nodeinfo[0][2])
    postorder(new_nodeinfo[0][2])
    
    answer = [preorder_list,postorder_list]

    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))