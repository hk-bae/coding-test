#이것이 코딩테스트다 375pg
#Flipkart 인터뷰

t = int(input())
results = []
for _ in range(t) :
  n,m = map(int,input().split())

  data = list(map(int,input().split()))
  golds = [[0] * m for _ in range(n)]

  for i in range(n) :
    for j in range(m) :
      golds[i][j] = data[i * m + j]
  
  
  # n행 m열
  d = [[0] * m for _ in range(n)]

  for i in range(n) :
    d[i][0] = golds[i][0]

  for j in range(1,m) :
    tmp = 0
    for i in range(n) :
      tmp = d[i][j-1]
      if i - 1 >= 0 :
        tmp = max(d[i-1][j-1], tmp)
      if i + 1 < n :
        tmp = max(d[i+1][j-1],tmp)

      d[i][j] = tmp + golds[i][j]
  
  result = 0
  for i in range(n) :
    result = max(result, d[i][m-1])

  results.append(result)


  for result in results :
    print(result)
