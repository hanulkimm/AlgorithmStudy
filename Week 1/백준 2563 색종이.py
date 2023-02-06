# 이번주에 배운 이차원 배열 사용
n = int(input())

arr = [[0]* 100 for _ in range(100)]

for _ in range(n):
    n,m = map(int, input().split())

    for i in range(n, n+10):
        for j in range(m, m+10):
            arr[i][j] += 1
ans = 0

for i in range(100):
    for j in range(100):
        if arr[i][j]>=1:
            ans += 1
print(ans)
