n = int(input())
arr = [0] * 1001 # 0~1001
mx_i = 0
mx = 0
for _ in range(n):
    l, h = map(int, input().split())
    arr[l] = h # 높이 추가
    if mx < h:
        mx = h
        mx_i = l

ans = 0
stk = []
for ch in arr[:mx_i+1]: # 최대높이 까지
    if stk:
        if stk[-1] < ch:
            stk.append(ch)
        ans += stk[-1]
    else:
        stk.append(ch)
        ans += stk[-1]
stk = []
for ch in arr[mx_i+1:][::-1]: # 최대높이까지 반대로
    if stk:
        if stk[-1] < ch:
            stk.append(ch)
        ans += stk[-1]
    else:
        stk.append(ch)
        ans += stk[-1]
print(ans)