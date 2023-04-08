import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)
## dfs + dp로 풀기
## dfs 시간초과

def dfs(i,j):
    if dp[i][j]: # 이미 방문했다면
        return dp[i][j] # 반환(이미 dfs 돌려져있음, 다시 dfs하는 것이 의미 무)
    dp[i][j]=1 # 일단 이동 표시
    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni,nj=i+di, j+dj
        if 0<=ni<n and 0<=nj<n and arr[ni][nj]>arr[i][j]: # 범위내, 조건 만족
            rtn = dfs(ni,nj) 
            dp[i][j] = max(dp[i][j], rtn+1) # 반환되는 값에 +1(이동 처리)하고 기존 값과 비교하기
    return dp[i][j]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0
dp = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i,j))
print(ans)
