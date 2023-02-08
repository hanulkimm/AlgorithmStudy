import sys

sys.stdin = open('input.txt', 'r')


# [1] (0,0) 기준으로 거리 구하는 함수 만들기
def lth(drt, x):
    if drt == 1:
        return x
    elif drt == 3:
        return width + height + width + height - x
    elif drt == 2:
        return height + width + width - x
    else:
        return width + x


# [2] 초기 설정
width, height = map(int, input().split())  # 가로, 세로
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dr, cx = map(int, input().split())  # 경비원의 방향, 위치
total_length = 2 * (width + height)  # 전체 둘레


ans = 0
for lst in arr:
    ndr = lst[0]
    nx = lst[1]

    a_length = lth(dr, cx)  # 원점에서 경비원의 거리
    b_length = lth(ndr, nx) # 원점에서 상점까지 거리

    if a_length < b_length:
        if b_length - a_length < total_length - (b_length - a_length):
            ans += b_length - a_length
        else:
            ans += total_length - (b_length - a_length)
    else:
        if a_length - b_length < total_length - (a_length - b_length):
            ans += a_length - b_length
        else:
            ans += total_length - (a_length - b_length)
print(ans)
