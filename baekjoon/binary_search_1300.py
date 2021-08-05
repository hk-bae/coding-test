n = int(input())
k = int(input())

start = 1
end = n * n
result = 0

while start <= end :
    mid = (start + end) // 2
    cnt = 0
    
    # 각 행에서 mid보다 작거나 같은 수의 개수를 센다.
    for i in range(1,n+1) :
        cnt += min( mid // i, n)
    
    # mid보다 작거나 같은 수의 개수가 k가 작으면
    if cnt < k :
        start = mid + 1
    else : 
        end = mid - 1
        result = mid
        
print(result)