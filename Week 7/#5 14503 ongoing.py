import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
si, sj, dr = map(int, input().split()) # 시작 좌표, 방향
arr = [list(map(int, input().split())) for _ in range(n)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
stk = []


ci, cj = si, sj
arr[ci][cj]=1
ans = 1
while True:
    ni, nj = ci + di[dr], cj + dj[dr]
    if 0<=ni<n and 0<=nj<m and arr[ni][nj]==0: # 범위내, 빈 칸, 미방문
        stk.append((ci,cj)) # 돌아올 자리
        ci, cj = ni, nj
        ans += 1 # 청소하는 칸 증가
        arr[ci][cj]=1

    else:
        for _ in range(3):
            flag = True
            dr = (dr+3)%4 #반시계 방향 90도
            ni, nj = ci + di[dr], cj + dj[dr]
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0:
                flag = False
                stk.append((ci, cj))
                ci, cj = ni, nj
                arr[ci][cj]=1
                ans += 1
                break
        if flag: # 주변 4칸 중 청소되지 않은 빈 칸 없음
            dr = (dr + 3) % 4
            if stk:
                ci,cj = stk.pop() # 한 칸 후진
                if arr[ci][cj]==1:
                    break
            else:
                break

print(ans)
