
t = int(input())

for _ in range(t) :
    data = input()

    res = 0
    cnt = 0 # 연속된 수의 개수

    for c in data :
        if c == 'O' :
            cnt += 1
        else :
            cnt = 0
        res += cnt

    print(res)