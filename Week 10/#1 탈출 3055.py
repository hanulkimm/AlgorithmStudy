import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def bfs(water_lst):
    while water_lst:
        wi,wj = water_lst.popleft()
        for di,dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nwi, nwj = wi+di, wj+dj
            if 0<=nwi<n and 0<=nwj<m and (arr[nwi][nwj]=='.' or arr[nwi][nwj]=='S'):
                if water_v[nwi][nwj]==0 or water_v[nwi][nwj] > water_v[wi][wj]+1:
                    water_v[nwi][nwj]=water_v[wi][wj]+1
                    water_lst.append((nwi,nwj))

def bfs_new(si,sj):
    v = [[0] * m for _ in range(n)]
    q = deque()
    q.append((si,sj))
    v[si][sj]=1

    while q:
        ci,cj=q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<m and (arr[ni][nj]=='.' or arr[ni][nj]=='D'):
                if v[ni][nj]==0 or v[nj][nj]>v[ci][cj]+1: # 고슴도치의 이동조건(최소 시간으로 이동)
                    if v[ci][cj]+1 < water_v[ni][nj]: # 물의 이동시간보다 적게 걸렸다면
                        v[ni][nj]=v[ci][cj]+1
                        q.append((ni,nj))
            if 0 <= ni < n and 0 <= nj < m and  arr[ni][nj] == 'D':
                if v[ni][nj] == 0 or v[nj][nj] > v[ci][cj] + 1:
                    v[ni][nj] = v[ci][cj] + 1
    return v[ei][ej]

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
print(arr)
water_lst = deque()
water_v = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j]=='*':
            water_lst.append((i,j))
            water_v[i][j]=1
        if arr[i][j]=='S':
            si, sj = i, j
        if arr[i][j]=='D':
            ei, ej = i, j
bfs(water_lst)

print(water_v)
print(bfs_new(si,sj))