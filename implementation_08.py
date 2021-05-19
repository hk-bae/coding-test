# 08. 문자열 재정렬
# 이것이 취업을 위한 코딩테스트다 with 파이썬, 322pg 

text = input()

num_sum = 0
alp_list = []

for ch in text :
  if 'A'<= ch <='Z' :
    alp_list.append(ch)
  else :
    num_sum += int(ch)

alp_list.sort()
#합이 없을 경우 더해주지 않음
if num_sum != 0 :
  alp_list.append(str(num_sum))
answer = "".join(alp_list)

print(answer)
