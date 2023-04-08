def dfs(i, cnt, st):
    global ans
    if int(st) > int(ans[:len(st)]): # 계산 중 ans보다 크다면
        return
    for num in range(2, m+1): # 나쁜 수열 판별하기
        if len(st)>=2*num:
            if st[len(st)-num:]==st[len(st)-2*num:len(st)-num]:
                return
    
    # 만약 길이 6: 
    
    if cnt==n:
        if int(ans) > int(st):
            ans = st
        return
    for j in range(1, 4):
        if v[j]==0: # 이전 숫자와 같지 않다면
            v[j]=1 # 선택 표시
            v[i]=0 # 이전 숫자 선택 해제
            dfs(j, cnt+1, st+str(j))
            v[j]=0
            v[i]=1

n = int(input())
m = n//2
v = [0] * 4
v[1]=1
ans = '3'*n #가장 큰 수열

dfs(1, 1, '1') # start, cnt, st
print(ans)