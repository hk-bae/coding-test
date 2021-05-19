s = input()

result = 0
for ch in s :
  num = int(ch)
  if result != 0 :
    if num == 1 or num == 0 :
      result += num
    else :
      result *= num
  else :
    result += num

print(result)
