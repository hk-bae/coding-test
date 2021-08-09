import sys
from collections import deque
import copy

input = sys.stdin.readline
    
n,k = map(int,input().split())
belt = deque(list(map(int,input().split()))) # 각 내구도를 갖는 벨트
robot = deque([0] * n) # 로봇
stage = 0
cnt = 0

while cnt < k :
    stage += 1
    # 벨트를 회전시킨다.
    belt.rotate(1) 
    robot.rotate(1)

    robot[n-1] = 0 # 벨트 회전 후 내리는 위치에 로봇이 존재한다면 내린다.

    # 먼저 들어온 로봇부터 이동할 수 있다면 이동한다.
    for i in range(n-2,-1,-1) :
        # 이동 가능한 경우
        if robot[i] != 0 and belt[i+1] > 0 and robot[i+1] == 0 :
            robot[i] = 0
            robot[i+1] = 1
            belt[i+1] -= 1
            if belt[i+1] == 0 :
                cnt += 1

    robot[n-1] = 0 # 내리는 위치에 로봇이 존재한다면 내린다.

    # 올리는 위치에 내구도가 0보다 크면 로봇을 올린다
    if belt[0] > 0 and robot[0] == 0 :
        robot[0] = 1
        belt[0] -= 1
        if belt[0] == 0 :
            cnt += 1


print(stage)    
                    

