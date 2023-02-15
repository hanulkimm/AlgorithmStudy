import sys

sys.stdin = open('input.txt', 'r')

## 시간 초과...##
# 아직 푸는 중

def p(st):
    n = len(st)
    m = n // 2
    if n % 2:
        if st[:m] == st[m+1:][::-1]: # 회문
            return 0
        else:
            return 2
    elif n % 2 == 0:
        if st[:m] == st[m:][::-1]: # 회문
            return 0
        else:
            return 2

t = int(input())
for tc in range(1, t+1):
    st = input()
    n = len(st)
    m = n // 2
    ans = p(st) # 회문 판정
    if ans != 0:
        st1 = ''
        st2 = ''
        for i in range(m):
            if st[i] != st[n-i-1]:
                if i == 0:
                    st1 += st[1:]
                    st2 += st[:n-1]
                    a, b = p(st1), p(st2)
                    if a == 0 or b == 0:
                        ans = 1
                else:
                    st1 += st[:i] + st[i+1:]
                    st2 += st[:n-1-i] + st[n-1-i+1:]
                    a, b = p(st1), p(st2)
                    if a == 0 or b == 0:
                        ans = 1

    print(ans)


    #     ans = 2
    #     new_st = ''
    #     for i in range(n):
    #         if i == 0:
    #             new_st = st[1:]
    #             if new_st == new_st[::-1]:
    #                 ans = 1
    #                 break
    #         elif i == n-1:
    #             new_st = st[:n-1]
    #             if new_st == new_st[::-1]:
    #                 break
    #         else:
    #             new_st = st[:i] + st[i+1:]
    #             if new_st == new_st[::-1]:
    #                 ans = 1
    #                 break
    # print(ans)