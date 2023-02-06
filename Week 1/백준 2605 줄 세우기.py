n = int(input())
lst = list(map(int, input().split())) # 이동 번호


st = list(range(1,n+1)) # 처음 학생 나열

for i in range(1, n): # 두번째 학생 부터
    save = st[i]
    move = lst[i]
    if move != 0: # 이동한다면
        for j in range(1, move+1):
            st[i-j+1] = st[i-j] # 앞 숫자들 이동시키고
            st[i-j] = save # 내 숫자 저장