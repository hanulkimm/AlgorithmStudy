## dp

n = int(input())
dp= [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n): # 집마다
    dp[i][0] = dp[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = dp[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = dp[i][2] + min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[n-1]))


## 백트래킹
## 시간초과 
def dfs(cnt, sm, used):
    global ans

    if sm>ans:
        return
    if cnt==n:
        ans = min(ans, sm)
        return
    for j in range(3):
        if j != used:
            dfs(cnt+1, sm+arr[cnt][j], j)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
mn = 0
for lst in arr:
    mn += min(lst)
ans = 1000*n
dfs(0,0,-1)
print(ans)