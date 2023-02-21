## 재귀함수 이용하기 ##

def p():
    if len(stk) == m:
        print(*stk)

    for i in range(1, n+1):
        if i not in stk:
            stk.append(i)
            p()
            stk.pop()

n, m = map(int, input().split())
stk = []
p()



