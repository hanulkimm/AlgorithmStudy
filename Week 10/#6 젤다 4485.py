from collections import deque

def bfs(i,j):
    q = deque()
    q.append((i,j))
    v[i][j]=arr[i][j]

    while q:
        ci,cj = q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<n:
                if v[ni][nj] > v[ci][cj] + arr[ni][nj]:
                    v[ni][nj] = v[ci][cj] + arr[ni][nj]
                    q.append((ni,nj))
tc = 1
while True:
    n = int(input())
    if n ==0:
        break
    else:
        arr = [list(map(int, input().split())) for _ in range(n)]
        INF = 1e9
        v = [[INF]*n for _ in range(n)]
        bfs(0,0)
        ans = v[n-1][n-1]
        print(f'Problem {tc}: {ans}')
        tc += 1