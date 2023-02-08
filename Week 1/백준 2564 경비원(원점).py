import sys

sys.stdin = open('input.txt', 'r')


# [1] (0,0) 기준으로 거리 구하는 함수 만들기
def lth(drt, x):
    if drt == 1:
        return x
    elif drt == 3:
        return x
    elif drt == 2:
        return height + x
    else:
        return width + x


# [2] 초기 설정
width, height = map(int, input().split())  # 가로, 세로
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dr, cx = map(int, input().split())  # 경비원의 방향, 위치
total_length = 2 * (width + height)  # 전체 둘레


a_length = lth(dr, cx)  # 원점에서 경비원의 거리
ans = 0
for lst in arr:
    ndr = lst[0]
    nx = lst[1]

    b_length = lth(ndr, nx) # 원점에서 상점까지 거리

    if dr == ndr:  # 4 가지
        if a_length < b_length:
            ans += b_length - a_length
        else:
            ans += a_length - b_length
    elif dr in [1, 4] and ndr in [2, 3]:  # 4가지
        length = a_length + b_length
        if length < total_length - length:  # 갈 수 있는 두 가지 경우 모두 고려하기
            ans += length
        else:
            ans += total_length - length
    elif ndr in [1, 4] and dr in [2, 3]:  # 4가지
        length = a_length + b_length
        if length < total_length - length:
            ans += length
        else:
            ans += total_length - length
    elif dr in [1, 4] and ndr in [1, 4]:  # 2가지(같은 경우는 이미 위에서 고려했으니까)
        if a_length < b_length:
            ans += b_length - a_length
        else:
            ans += a_length - b_length
    elif dr in [2, 3] and ndr in [2, 3]:  # 2 가지
        if a_length < b_length:
            ans += b_length - a_length
        else:
            ans += a_length - b_length

print(ans)
