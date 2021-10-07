def solution(user_info) :
    user_info.sort()
    result = []
    for age,_,name in user_info :
        result.append((age,name))
    return result

n = int(input())
user_info = []
for i in range(n) :
    age_str,name = input().split()
    age = int(age_str)
    user_info.append((age,i,name))
    
result = solution(user_info)

for age,name in result :
    print(age,name)