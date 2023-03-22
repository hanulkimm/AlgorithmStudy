import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
def bfs(i,j,v):
    q = deque([(i,j)])
    while q:
        ci,cj = q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)): # 상하좌우
            ni,nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<n and v[ni][nj]==0 and arr[ni][nj]>level:
                v[ni][nj]=1
                q.append((ni,nj))

def cnt(level):
    tmp = 0
    v = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] > level and v[i][j]==0:
                tmp += 1
                bfs(i,j,v)
    return tmp

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
mx = 0
for lst in arr:
    for ch in lst:
        if mx < ch:
            mx = ch
ans = 0
for level in range(0, mx): # 아무 지역도 물에 잠기지 않는 경우 고려해서 0부터 시작
    count = cnt(level)
    if ans < count:
        ans = count
print(ans)