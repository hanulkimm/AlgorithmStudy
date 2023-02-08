import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
m = int(input())

# [1] 초기 설정
di = [1, 0, -1, 0] # 아래, 오른쪽, 위쪽, 왼쪽
dj = [0, 1, 0, -1]

dr = 0  # 초기 설정(아래부터 시작)

arr = [[0] * n for _ in range(n)]

i = 0 #맨 뒤 숫자부터 시작하기
j = 0

for cnt in range(n*n, -1, -1):
    arr[i][j] = cnt
    ni, nj = i + di[dr], j + dj[dr]
    if 0<=ni<n and 0<=nj<n and arr[ni][nj] == 0:
        i, j = ni, nj
    else:
        dr = (dr+1) % 4
        i += di[dr]
        j += dj[dr]

for lst in arr:
    print(*lst, end='\n')

for i in range(n):
    for j in range(n):
        if arr[i][j] == m:
            print(i+1, j+1)


