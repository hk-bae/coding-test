import sys

sys.setrecursionlimit(10**6)

class Node :
    def __init__(self,alp,nexts,loc,num,end) :
        self.alp = alp
        self.nexts = nexts
        self.loc = loc
        self.num = num
        self.end = end

def addToTree(node,i,word) :
    
    if i >= len(word) :
        return
    
    find = False
    for next in node.nexts :
        if next.alp == word[i] :
            next.num += 1
            addToTree(next,i+1,word)
            find = True
            
    if not find :
        next = Node(word[i],[],node.loc + 1,1,0)
        node.nexts.append(next)
        addToTree(next,i+1,word)
    
    # 마지막 단어일 경우
    if i == len(word) - 1 :
        next.end += 1 

        
def search_tree(node) :
    global result

    if node.num == 1 :
        result += node.loc
        return
    elif node.end == 1 :
        result += node.loc
    
    for next in node.nexts :
        search_tree(next)
    

def solution(words):
    global result
    tree = dict()
    
    
    # 각 알파벳을 시작으로 하는 노드 생성
    for i in range(26) :
        ch = chr(ord('a')+i)
        nexts = []
        tree[ch] = Node(ch,nexts,1,0,0)
    
    # 각 단어에 대하여 
    for word in words :
        start_alp = word[0]
        start_node = tree[start_alp] # 시작 노드
        start_node.num += 1 # 개수 1 증가
        if len(word) == 1 :
            start_node.end += 1 
            continue
        addToTree(start_node,1,word)
        
    # 입력 개수 찾기
    result = 0
    for i in range(26) :
        ch = chr(ord('a')+i)
        
        if tree[ch].num > 0 :
            search_tree(tree[ch])
    
    
    
    return result