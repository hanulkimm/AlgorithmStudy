import sys
sys.stdin = open('input.txt', 'r')

w, h = map(int, input().split())

si, sj = map(int, input().split())
t = 8

di, dj = 1, 1

cnt = 0
i, j = si, sj
while cnt < 8:
    ni, nj = i + di, j + dj
    if 0<ni<w and 0<nj<h:
        cnt += 1
    elif nj == h:
        di, dj = -1, -1
        cnt += 1
    elif ni == w:
        di, dj = -1, 1
        cnt += 1
    elif nj == 0:
        di, dj =




