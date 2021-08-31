import re

class Node :
    def __init__(self,url,basic,links,link_score) :
        self.url = url
        self.basic = basic # 기본 점수
        self.links = links # 외부 링크 배열
        self.link_score = link_score
    
        
def calcLinkScore(url) :
    global graph
    tmp = 0
    cnt = len(graph[url].links)
    if cnt != 0 :
        tmp = graph[url].basic / cnt
        
    for link in graph[url].links :
        if link in graph.keys() :
            graph[link].link_score += tmp
    
    
        
def solution(word, pages):
    global graph
    graph = {}
    urls = []
    word = word.lower()
    for page in pages : # 각 페이지에 대해 기본점수, 외부링크수, [외부링크url] 저장
        A = list(page.split("\n")) 
        node = Node(None,None,None,0)
        links = [] # 외부 링크 저장
        basic = 0 # 기본 점수
        for string in A :  
            string = string.strip()
            
            # url 찾기
            if string.startswith("<meta property=") : 
                tmp = list(string.split('"')) # " 기준으로 split
                
                node.url = tmp[-2]
                urls.append(node.url)
            
            # body 부분에 대하여 기본 점수 계산
            if not string.startswith("<") or string.startswith("<a href"): 
                body_words = re.split("<a href=|></a>",string)
                for body_word in body_words :
                    if body_word.startswith('"https://') :
                        tmp = body_word.split('"')
                        links.append(tmp[-2])
                    else :
                        page_word = re.split("[^a-zA-Z]",body_word)
                        for w in page_word :
                            w = w.lower()
                            if w == word :
                                basic += 1
                            
        node.links = links
        node.basic = basic
        graph[node.url] = node

    
    # 링크점수 계산
    for url in urls :
        calcLinkScore(url)
        
    max_value = 0
    idx = 0
    for i,url in enumerate(urls) :
        
        matching_score = graph[url].basic + graph[url].link_score
        if max_value < matching_score :
            max_value = matching_score
            idx = i
        
    return idx

print(solution("Muzi",["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))
