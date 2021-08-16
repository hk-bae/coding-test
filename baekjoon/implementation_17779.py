import sys
input = sys.stdin.readline

def find_min(data,x,y,d1,d2) :
    global n

    value1,value2,value3,value4,value5 = 0,0,0,0,0

    # 1번 구역
    for i in range(x+d1) :
        for j in range(0,y+1) :
            if data[i][j] != 5 :
                data[i][j] = 1
            else : 
                break

    # 2번 구역
    for i in range(x+d2+1) :
        for j in range(n-1,y,-1) :
            if data[i][j] != 5 :
                data[i][j] = 2
            else :
                break

    # 3번 구역
    for i in range(x+d1,n) :
        for j in range(y-d1+d2) :
            if data[i][j] != 5 :
                data[i][j] = 3
            else :
                break

    # 4번 구역
    for i in range(x+d2+1,n) :
        for j in range(n-1,y-d1+d2-1,-1) :
            
            if data[i][j] != 5 :
                data[i][j] = 4
            else :
                break

    for i in range(n) :
        for j in range(n) :
            if data[i][j] == 1 :
                value1 += graph[i][j]
            elif data[i][j] == 2 :
                value2 += graph[i][j]
            elif data[i][j] == 3 :
                value3 += graph[i][j]
            elif data[i][j] == 4 :
                value4 += graph[i][j]
            else :
                value5 += graph[i][j]

    max_value = max(value1,value2,value3,value4,value5)
    min_value = min(value1,value2,value3,value4,value5)

    # for i in range(n) :
    #     for j in range(n) :
    #         print(data[i][j],end= " ")
    #     print()
    # print()


    return max_value - min_value
                


n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
res = 1e9

# 시작할 (x,y) 정하기
for x in range(n-2) : # 가능한 x 범위 0...n-3
    for y in range(1,n-1) : # 가능한 y 범위 1...n-2
        # d1 과 d2를 정하기
        d1_first = True
        d1,d2 = 1,1
        while True :
            tmp = [[0] * n for _ in range(n)] # 이번 구역
            tmp[x][y] = 5
            # print("#",d1,d2)
            for i in range(1,d1+1) : 
                tmp[x+i][y-i] = 5 # 1번 경계선
                tmp[x+d2+i][y+d2-i] = 5# 4번 경계선
                 
            for i in range(1,d2+1) : 
                tmp[x+i][y+i] = 5 # 2번 경계선
                tmp[x+d1+i][y-d1+i] = 5# 3번 경계선
            
            # for i in range(n) :
            #     for j in range(n) :
            #         print(tmp[i][j],end= " ")
            #     print()
            # print()

            res = min(res,find_min(tmp,x,y,d1,d2))

            if d1_first :
                if x + (d1+1) + d2 < n and y - (d1+1) >= 0 :
                    d1 += 1 # d1 부터 증가
                elif x + d1 + (d2+1) < n and y + (d2+1) < n :
                    d2 += 1
                else :
                    if d1 < 2 or x + (d1-1) + 2 < n and y + 2 >= n : break
                    d1 -= 1
                    d2 = 2
                    d1_first = False
                    continue
            else :
                if x + d1 + (d2+1) < n and y + (d2+1) < n :
                    d2 += 1 # d2 증가
                elif d1 > 1 : 
                    # d1을 1 감소 시킨 후 다시 반복
                    d1 -= 1
                    d2 = 2
                    continue
                else :
                    break

      
print(res)
            

            