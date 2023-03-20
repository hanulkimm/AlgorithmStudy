import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
si, sj, dr = map(int, input().split()) # 시작 좌표, 방향
arr = [list(map(int, input().split())) for _ in range(n)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
v = [[0]*m for _ in range(n)]
ans = 0

ci, cj = si, sj
if arr[ci][cj]==0:
    ans += 1
    v[ci][cj]=1
while True:
    flag = True
    for _ in range(4):
        dr = (dr+3)%4 # 반시계방향
        ni,nj = ci+di[dr], cj+dj[dr]
        if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0 and v[ni][nj]==0:
            ans += 1
            v[ni][nj]=1
            ci,cj = ni,nj
            flag=False
            break
    if flag: # 주변 4칸 중 청소되지 않은 빈 킨이 없는 경우
        dr = (dr+2)%4 # 후진 방향
        ni,nj = ci+di[dr], cj+dj[dr]
        if arr[ni][nj]==1: # 뒤 칸이 벽인 경우
            break
        else:
            ci,cj = ni,nj
            dr = (dr-2)%4 # 후진 방향 다시 되돌려놓기!!

print(ans)
