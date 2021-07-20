s = input()

# 1 -> 1
# 2 -> 1
# 3 -> 2
# 4 -> 2
# 5 -> 3
# 6 -> 3

num = s[0]
count = 0 # 숫자가 변하는 횟수
for i in range(1,len(s)) :
  if num != s[i] :
    count += 1
    num = s[i]

result = int(round(count / 2,1))
print(result)
