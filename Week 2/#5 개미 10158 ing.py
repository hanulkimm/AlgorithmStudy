import sys
sys.stdin = open('input.txt', 'r')

w, h = map(int, input().split())

si, sj = map(int, input().split())
t = int(input())

di, dj = 1, 1 # 기본 방향(위로 45도)

cnt = 0
i, j = si, sj
while cnt < t: # 주어진 시간 동안
    ni, nj = i + di, j + dj
    cnt += 1
    i, j = ni, nj
    if nj == h: # 윗면 닿으면
        di, dj = -1, -1
    elif ni == w: # 오른쪽 면 닿으면
        di, dj = -1, 1
    elif nj == 0: # 바닥에 닿으면
        di, dj = -1, 1
    elif ni == 0: # 왼쪽 면에 닿으면
        di, dj = 1, 1

print(i, j)
