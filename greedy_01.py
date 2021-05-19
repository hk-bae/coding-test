n = int(input())  # 1<= n <= 100,000
fears = list(map(int, input().split()))
fears.sort()

# 1 2 2 2 3

count = 0  # 떠날 수 있는 그룹 수
now = 0  # 임시로 저장할 현재 그룹의 인원 수
for fear in fears:
    now += 1
    if fear <= now:
        count += 1
        now = 0

print(count)

