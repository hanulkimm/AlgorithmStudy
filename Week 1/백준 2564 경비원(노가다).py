## 풀리긴 하지만 추천하지 않는 노가다 코드...##
## 이렇게 풀지 말기 ##

import sys

sys.stdin = open('input.txt', 'r')


width, height = map(int, input().split()) # 가로, 세로
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dr, x = map(int, input().split()) # 경비원의 방향, 위치
total_length = 2*(width + height) # 전체 둘레

total_cnt = 0
for lst in arr:
    ndr = lst[0]
    nx = lst[1]

    cnt = 0
    if dr == 2:
        if ndr == 2: # 같은 방향 일 때
            if x > nx:
                cnt += x - nx
            else:
                cnt += nx - x

        if ndr == 3:
            if x + height - nx < total_length - (x + height - nx):
                cnt += x + height - nx
            else:
                cnt += total_length - (x + height - nx)
        if ndr == 1:
            if x + height + nx < total_length - (x + height + nx):
                cnt += x + height + nx
            else:
                cnt += total_length - (x + height + nx)
        if ndr == 4:
            if width - x + height - nx < total_length - (width - x + height - nx):
                cnt += width - x + height - nx
            else:
                cnt += total_length - (width - x + height - nx)

    if dr == 3:
        if ndr == 3: # 같은 방향 일 때
            if x > nx:
                cnt += x - nx
            else:
                cnt += nx - x
        if ndr == 1:
            if x + nx < total_length - (x + nx):
                cnt += x + nx
            else:
                cnt += total_length - (x + nx)
        if ndr == 4:
            if x + width + nx < total_length - (x + width + nx ):
                cnt += x + width + nx
            else:
                cnt += total_length - (x + width + nx )
        if ndr == 2:
            if height - x + nx < total_length - (height - x + nx):
                cnt += height - x + nx
            else:
                cnt += total_length - (height - x + nx)
    if dr == 4:
        if ndr == 4: # 같은 방향 일 때
            if x > nx:
                cnt += x - nx
            else:
                cnt += nx - x
        if ndr == 2:
            if height - nx + width - x < total_length - (height - nx + width - x):
                cnt += height - nx + width - x
            else:
                cnt += total_length - (height - nx + width - x)
        if ndr == 3:
            if x + width + nx < total_length - (x + width + nx):
                cnt += x + width + nx
            else:
                cnt += total_length - (x + width + nx)
        if ndr == 1:
            if width - nx + x < total_length - (width - nx + x ):
                cnt += width - nx + x
            else:
                cnt += total_length - (width - nx + x )
    if dr == 1:
        if ndr == 1: # 같은 방향 일 때
            if x > nx:
                cnt += x - nx
            else:
                cnt += nx - x
        if ndr == 4:
            if width - x + nx < total_length - (width - x + nx):
                cnt += width - x + nx
            else:
                cnt += total_length - (width - x + nx)
        if ndr == 2:
            if x + height + nx < total_length - (x + height + nx):
                cnt += x + height + nx
            else:
                cnt += total_length - (x + height + nx)
        if ndr == 3:
            if x + nx < total_length - (x + nx):
                cnt += x + nx
            else:
                cnt += total_length - (x + nx)

    total_cnt += cnt


print(total_cnt)