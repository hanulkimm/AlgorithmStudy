import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def visit(i, j): # bfs
    global v
    global cnt 
    cnt += 1 # 덩어리 하나 추가
    v[i][j] = 1
    q = deque()
    q.append((i, j))
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):  # 상하좌우
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] != 0 and v[ni][nj] == 0:
                v[ni][nj] = 1
                q.append((ni, nj))


def split(arr):  # 몇 개의 덩어리인지 판별 함수
    global v
    global cnt
    cnt = 0
    v = [[0] * m for _ in range(n)]
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if v[i][j] == 0 and arr[i][j] != 0:
                visit(i, j)
    return cnt


def melt(arr):  # 빙산 녹이기
    arr_temp = [[0] * m for _ in range(n)]
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if arr[i][j] != 0:
                melt_num = 0
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = i + di, j + dj
                    if arr[ni][nj] == 0:
                        melt_num += 1
                if arr[i][j] - melt_num < 0:
                    arr_temp[i][j]=0
                else:
                    arr_temp[i][j] = arr[i][j] - melt_num

    for nwi in range(1, n - 1):
        for nwj in range(1, m - 1):
            arr[nwi][nwj] = arr_temp[nwi][nwj]


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
while True:
    if split(arr) >= 2: # 빙산 덩어리 2개 이상
        break
    if split(arr) == 0: # 다 녹은 경우
        ans = 0
        break
    melt(arr) # 빙산 녹이기
    ans += 1 # 시간(년) +1
print(ans)
