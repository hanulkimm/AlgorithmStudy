# 재귀
def dfs(i, total, plus, minus, multiply, divide):
    global mx, mn
    if i == n:
        mx = max(mx, total)
        mn = min(mn, total)
    if plus:
        dfs(i+1, total+lst[i], plus-1,minus, multiply, divide) # 다음 숫자 더해주고 연산자 cnt 하나 빼주기
    if minus:
        dfs(i + 1, total - lst[i], plus, minus-1, multiply, divide)
    if multiply:
        dfs(i+1, total*lst[i], plus, minus,multiply-1, divide)
    if divide:
        dfs(i+1, int(total/lst[i]), plus, minus, multiply, divide-1)

n = int(input())
lst = list(map(int, input().split())) # 숫자 리스트
op = list(map(int, input().split())) # 사칙연산 개수

mx = -1e9
mn = 1e9

dfs(1, lst[0], op[0], op[1], op[2], op[3])
print(mx)
print(mn)