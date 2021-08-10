def rotate_clock(l) :
    global graph
    n = 8
    size = pow(2,l) # 격자 크기

    result = [[0 for _ in range(n)] for _ in range(n)]
    # 2^l x 2^l 으로 나눠야함
    for i in range(0,n,size) :
        for j in range(0,n,size):
            # 각 격자에 대하여 회전
            for s in range(0,size) :
                for t in range(0,size) :
                    result[i+size-t-1][j+s] = graph[i+s][j+t] 
    

    graph = result

graph = [list(map(int,input().split())) for _ in range(8)]
rotate_clock(1)
print()
for i in range(8) :
    for j in range(8) :
        print(graph[i][j],end= ' ')
    print()

