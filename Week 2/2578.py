import sys

sys.stdin = open('input.txt', 'r')


def count(arr):
    sm = 0
    for _ in range(2):
        for lst in arr:
            if lst == [1] * 5:
                sm += 1
        arr = list(zip(*arr))

    cnt = cnt2 = 0
    for i in range(5):
        if arr[i][i] == 1:
            cnt += 1
        if arr[i][4 - i] == 1:
            cnt2 += 1
    if cnt == 5 or cnt2 == 5:
        sm += 1
    return sm


bingo = [[0] * 5 for _ in range(5)]

arr_me = [list(map(int, input().split())) for _ in range(5)]
lst_ans = []  # 사회자가 부르는 숫자
for _ in range(5):
    lst = list(map(int, input().split()))
    for n in lst:
        lst_ans.append(n)
print(lst_ans)

cnt = 0
# while cnt < 3:
for key in lst_ans:
    for i in range(5):
        for j in range(5):
            if arr_me[i][j] == key:
                bingo[i][j] = 1
                cnt = count(bingo)
                print(key, cnt)

# bingo = [[0]*5 for _ in range(5)]
#
# sm = 0
# for num in lst_ans:
#     for i in range(5):
#         if bingo[i][::] == [1] * 5:
#             sm += 1
#         if bingo[::][i] == [1] * 5:
#             sm += 1
#
#         if sm == 3:
#             print(num)
#             break
#         for j in range(5):
#             if arr_me[i][j] == num:
#                 bingo[i][j] = 1
#                 break
#
