import sys
sys.stdin = open('input.txt', 'r')

def spread(i, j):
    cnt = 0
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] != -1:  # 범위내, 공기청정기 아님
            cnt += 1
            v[ni][nj] += int(arr[i][j] / 5)
    arr[i][j] = arr[i][j] - int(arr[i][j] / 5) * cnt

def clean(i,j,k):
    ci, cj = i, j + 1
    dr = 0
    keep= use = 0
    while True:
        ni, nj = ci + di[dr], cj + dj[dr]
        if 0 <= ni < n and 0 <= nj < m:
            if arr[ni][nj] == -1:  # 다 돌았을 때
                arr[ci][cj]=use
                break
            else:
                keep = arr[ci][cj] # 현재 내 값 저장
                arr[ci][cj]=use # 현재 값 갱신
                use = keep # 사용할 값 갱신
                ci,cj = ni,nj
        else:
            if k: # 2번째 경우(아래에서 바람) - 우하좌상
                dr = (dr+3)%4
            else: # 위에서 바람 우상좌하
                dr = dr + 1
            ni, nj = ci + di[dr], cj + dj[dr]
            if 0 <= ni < n and 0 <= nj < m:
                if arr[ni][nj] == -1:  # 다 돌았을 때
                    arr[ci][cj] = use
                    break
                else:
                    keep = arr[ci][cj]
                    arr[ci][cj] = use
                    use = keep
                    ci, cj = ni, nj
            else:  # 다 못 돌았는데 더 못갈때
                arr[ci][cj] = use
                break

n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for _ in range(t):
    # 미세먼지 lst
    clear = []
    for i in range(n):
        if arr[i][0] == -1:
            clear.append((i, 0))

    # [1] 미세먼지 확산
    v = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                spread(i, j)
    for i in range(n):
        for j in range(m):
            if (i,j) not in clear:
                arr[i][j] = arr[i][j] + v[i][j]

    # [2] 공기청정기 작동
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]

    for k in range(2):
        i, j = clear.pop(0)
        clean(i,j,k)

ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j]!=-1:
            ans += arr[i][j]
print(ans)
