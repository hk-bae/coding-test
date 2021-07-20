n = input()

nums = []
answer = "-1"
sum_value = 0
has_zero = False

for i in range(len(n)) :
    value = int(n[i])
    nums.append(value)
    sum_value += value
    if value == 0 :
      has_zero = True

if sum_value % 3 == 0 and has_zero :
    nums.sort(reverse = True)
    answer = "".join(str(_) for _ in nums)
    
print(answer)

