import math
# 성냥이 n개일 때 만들 수 있는 최소 숫자
# dp[n] = min(dp[i] * 10 + dp[n-i] where dp[i] * 10 ! = 0, dp[n-i]*10 + dp[i] where dp[n-i] * 10 ! = 0)
# for i in range(2, n//2)

dp = [''] * 101 
dp[2],dp[3],dp[4],dp[5],dp[6],dp[7] = '1','7','4','2','0','8'

def get_max_value(num) :
    max_value = ''
    if num % 2 == 0 :
        max_value = '1'* (num // 2)
    else :
        max_value = '7' + '1' * (num//2 - 1)

    return max_value

def get_min_value(num) : 

    # Bottom up
    for k in range(8,num+1) :
        for i in range(2,8) :
            if k - i < 2 : continue
            first = ''
            second = ''
            if dp[i] == '0' and dp[k-i] == '0' :
                continue
            elif dp[i] == '0' :
                first = '6' + dp[k-i]
                second = dp[k-i] + dp[i]
            elif dp[k-i] == '0' :
                first = dp[i] + dp[k-i]
                second = '6' + dp[i]                                
            else :
                first = dp[i] + dp[k-i]
                second = dp[k-i] + dp[i]

            min_value = min(first,second)

            length = len(dp[k])
            new_length = len(min_value)
            if dp[k] == '' :
                dp[k] = min_value
            elif length > new_length :
                dp[k] = min_value
            elif new_length == length :
                dp[k] = min(dp[k],min_value)
            

            
     

def solution(case) :
    result = []

    max_num = max(case)
    get_min_value(max_num)

    # 모든 케이스에 대하여 수행
    for num in case :
        result.append((dp[num],get_max_value(num)))

    return result
       
        
        
        


t = int(input())
case = []
for _ in range(t) :
    case.append(int(input()))
    
    

for min_value,max_value in solution(case):
    print(min_value if min_value != '0' else '6',max_value)
    