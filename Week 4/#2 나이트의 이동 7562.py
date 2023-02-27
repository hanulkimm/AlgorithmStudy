import sys
sys.stdin = open('input.txt', 'r')

def bfs(si, sj, ei, ej):
    global cnt
    q = []
    q.append((si,sj))
    while q:
        ci, cj = q.pop(0)
        if (ci,cj)==(ei,ej):
            cnt = v[ci][cj]
            break
        for di, dj in ((-2,1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1,-2), (-2, -1)):
            ni, nj= ci+di, cj+dj
            if 0<=ni<l and 0<=nj<l and v[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj]+1

t = int(input())
for tc in range(1, t+1):
    l = int(input())
    v = [[0]*l for _ in range(l)]
    si,sj = map(int, input().split())
    ei, ej = map(int, input().split())
    cnt = 0
    bfs(si, sj, ei, ej)
    print(cnt)