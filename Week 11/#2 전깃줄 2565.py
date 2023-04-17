n = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(n)])
dp = [1] * n
for i in range(1,n):
    for j in range(i):
        if arr[j][1] < arr[i][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))

# 참고
## 증가하는 부분 수열
## 백준 11053
n = int(input())
lst = list(map(int, input().split()))
dp = [1] * n
for i in range(1,n):
    for j in range(i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))