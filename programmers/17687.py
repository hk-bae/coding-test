
def solution(n, t, m, p):
    answer = ''
    
    dic = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    
    num = 0 # 게임을 시작할 숫자
    cnt = 0
    order = 1 # 차례
    # t개의 숫자를 저장할 때 까지 진행
    while cnt < t :
        
        # 수에 대한 n진법을 계산
        num_n = []
        
        tmp = num 
        while True : 

            num_n.append(tmp % n)
            tmp = tmp // n
            if tmp == 0 :
                break
                
        
        while num_n :
            if order == p : # 자기 차례라면
                answer += dic[num_n.pop()]
                cnt += 1
                if cnt == t : break
            else :
                num_n.pop()
                
                
            order += 1
            if order > m : order = 1
            
        if cnt == t : break    
        
        
        num += 1 
         
        
        
    return answer