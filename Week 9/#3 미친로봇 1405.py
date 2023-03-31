def dfs(i,j, cnt, p):
    global ans
    if cnt==n:
        ans += p
        return
    for di,dj,dr in ((0,1,0),(0,-1,1),(1,0,2),(-1,0,3)):
        ni,nj = i+di,j+dj
        if 0<=ni<2*n+1 and 0<=nj<2*n+1 and v[ni][nj]==0 and lst[dr]: # 범위내, 미방문, 확률 0 아님
            v[ni][nj]=1
            dfs(ni,nj,cnt+1, p*lst[dr])
            v[ni][nj]=0

n, *lst = map(int, input().split())
for i in range(4):
    lst[i] = lst[i]/100
v = [[0]*(2*n+1) for _ in range(2*n+1)] # 방문 표시용 2차원 배열 생성
si,sj = n, n # 중간에 시작위치
v[si][sj]=1 # 방문 표시
ans = 0
dfs(si,sj, 0, 1) # 시작좌표, 이동 횟수, 확률
print(ans)