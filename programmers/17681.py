def solution(n, arr1, arr2):
    answer = []

    for i in range(n) :
        num = arr1[i]
        binary_num = bin(num)
        string = str(binary_num)
        string_list = list(string[2:])
        
        list1 = [' '] * n 
        diff = n - len(string_list)
        for j in range(len(string_list)) :
            if string_list[j] == "1" :
                list1[j+diff] = '#'
                
        num = arr2[i]
        binary_num = bin(num)
        string = str(binary_num)
        string_list = list(string[2:])
        
        list2 = [' '] * n 
        diff = n - len(string_list)
        for j in range(len(string_list)) :
            if string_list[j] == "1" :
                list2[j+diff] = '#'
                
        new_string = ''
        for j in range(n) :
            if list1[j] == " " and list2[j] == " " :
                new_string += " "
            else :
                new_string += "#"
                
        answer.append(new_string)
        
        
     
    return answer

arr1=[9, 20, 28, 18, 11]
arr2=[30, 1, 21, 17, 28]

print(solution(5,arr1,arr2))

# 비트연산 이용
def solution2(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = bin(arr1[i]|arr2[i])[2:] # or 연산으로 바로 계산 
        b = '0'*(n-len(a)) + a # 부족한 길이 0 채워넣기 
        b = b.replace('1', '#') 
        b = b.replace('0', ' ')
        answer.append(b)
    return answer