import sys

sys.stdin = open('input.txt', 'r')
from collections import deque

t = int(input())
for tc in range(1, t + 1):
    m, n = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    v = [[0] * m for _ in range(n)] # 방문표시
    fire_q = deque() # 불 
    q = deque() # 사람
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '@':
                q.append((i, j, 0)) # 좌표랑 시간
                v[i][j] = 1
            if arr[i][j] == '*':
                fire_q.append((i, j, 0))
    ans = 0
    flag = False
    while True:
        while fire_q and fire_q[0][2] == ans: # 시간 맞춰서 bfs 돌리기
            fi, fj, _ = fire_q.popleft()
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nfi, nfj = fi + di, fj + dj
                if 0 <= nfi < n and 0 <= nfj < m and (arr[nfi][nfj] == '.' or arr[nfi][nfj] == '@'): # 빈 자리거나 사람이 있거나(사람은 어차피 움직이니까)
                    arr[nfi][nfj] = '*'
                    fire_q.append((nfi, nfj, ans + 1))
        while q and q[0][2] == ans:
            ci, cj, _ = q.popleft()
            if ci == 0 or cj == 0 or ci == n - 1 or cj == m - 1: # 가장자리 도착하면 
                print(ans + 1) # 탈출하는 시간 +1
                flag = True
                break
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = ci + di, cj + dj
                if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == '.' and v[ni][nj] == 0: # 범위내, 빈 공간, 방문 안함 조건 만족하면
                    arr[ni][nj] = '@' 
                    if arr[ci][cj] != '*': # 불이 올 자리면
                        arr[ci][cj] = '.' # 빈 공간 표시 안 하기
                    v[ni][nj] = 1 # 방문 표시
                    q.append((ni, nj, ans + 1))
        ans += 1
        if flag:
            break
        if not q: # 가장자리까지 도달못했는데 더 이상 갈 공간 없으면
            print("IMPOSSIBLE")
            break
