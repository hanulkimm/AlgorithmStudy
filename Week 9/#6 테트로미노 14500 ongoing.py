import sys

sys.stdin = open('input.txt', 'r')


def dfs(i, j, cnt, sm):
    global ans
    if cnt == 4:
        ans = max(ans, sm)
        return
    else:
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and v[ni][nj] == 0:
                if cnt == 2:  # 산 모양 만들어주기
                    v[ni][nj] = 1
                    dfs(ni, nj, cnt + 1, sm + arr[ni][nj])
                    v[ni][nj] = 0
                v[ni][nj] = 1
                dfs(ni, nj, cnt + 1, sm + arr[ni][nj])
                v[ni][nj] = 0


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
v = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        v[i][j] = 1
        dfs(i, j, 1, arr[i][j])
        v[i][j] = 0
print(ans)
