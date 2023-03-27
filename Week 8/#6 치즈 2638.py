import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
def cheese(arr): # 치즈 유무 판정
    for i in range(1, n-1):
        for j in range(1, m-1):
            if arr[i][j]==1:
                return True

def bfs(arr): # 치즈 범위 밖에 있는 빈 공간표시
    si,sj = 0,0
    q = deque()
    q.append((si,sj))
    arr[si][sj]=2
    while q:
        ci, cj = q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)): # 상하좌우
            ni,nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<m and arr[ni][nj]==0:
                arr[ni][nj]=2
                q.append((ni,nj))

def melt(arr): # 치즈 녹이기
    tmp = [[1]*m for _ in range(n)]
    for i in range(1, n-1): # 가장 자리는 없음
        for j in range(1,m-1):
            if arr[i][j]==1:
                num = 0
                for di,dj in ((-1,0),(1,0),(0,-1),(0,1)): # 상하좌우
                    ni,nj = i+di, j+dj
                    if 0<=ni<n and 0<=nj<m and arr[ni][nj]==2: # 전체 범위 내이고 치즈 범위 밖
                        num += 1
                if num>=2:
                    tmp[i][j]=0
    for i in range(n):
        for j in range(m):
            if tmp[i][j]==0:
                arr[i][j]=0
            if arr[i][j]==2: # 다시 빈 공간으로 표시
                arr[i][j]=0


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
while cheese(arr):
    bfs(arr)
    melt(arr)
    ans += 1
print(ans)