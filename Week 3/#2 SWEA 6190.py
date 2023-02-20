import sys
sys.stdin = open('input.txt', 'r')

# 단조 증가: 숫자 자릿수가 단순하게 증가(숫자가 같아도 되고 한 자리도 가능)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = list(map(int, input().split()))

    mlst = [] # ai * aj (단조 증가하는 수 후보들)
    for i in range(n):
        for j in range(n):
            if i != j:
                mlst.append(lst[i]*lst[j])
    mlst = list(map(str, set(mlst))) # 중복 제거
    
    ans = -1
    
    for i in mlst:
        flag = 'T'
        if len(i) == 1: # 한 자릿수 일 때
            if ans < int(i):
                ans = int(i)
        else:
            for j in range(len(i)-1):
                if i[j] > i[j+1]: # 단조가 아니면 flag 조건 걸기
                    flag = 'F'
                    break
            if flag != 'F': # 단조일 때
                if ans < int(i):
                    ans = int(i)
    print(f'#{tc} {ans}')