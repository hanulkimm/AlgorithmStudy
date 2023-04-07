import sys
sys.stdin = open('input.txt', 'r')
## dfs + dp로 풀기
## dfs 시간초과

def dfs(i,j):
    if dp[i][j]:
        return dp[i][j]
    dp[i][j]=1
    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni,nj=i+di, j+dj
        if 0<=ni<n and 0<=nj<n and arr[ni][nj]>arr[i][j]:
            dp[i][j] = max(dp[i][j], dfs(ni,nj)+1)
    return dp[i][j]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0
dp = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i,j))
print(ans)
