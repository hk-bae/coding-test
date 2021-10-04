import sys

input = sys.stdin.readline

def solution(s1,s2) :
    n1 = len(s1)
    n2 = len(s2)
    # dp[i][j] : s1의 i번째 문자열, s2의 j번째 문자열까지 비교했을 때의 결과
    # (if s1[i] = s2[j]) : dp[i][j] = dp[i-1][j-1] + 1
    # (if s1[i] != s2[j]) : dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)] 
    
    for i in range(1,n1+1) :
        for j in range(1,n2+1) :
            if s1[i-1] == s2[j-1] :
                dp[i][j] = dp[i-1][j-1] + 1
            else :
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[n1-1][n2-1]
    

s1 = input()
s2 = input()
print(solution(s1,s2))