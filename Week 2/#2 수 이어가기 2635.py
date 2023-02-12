n = int(input())

ans = []
mx = 0
for i in range(1, n + 1):
    cnt = 2
    lst = [n, i]
    while True:
        dif = lst[-2] - lst[-1]
        if dif >= 0: # 음의 정수가 아닐 떄
            lst.append(dif)
            cnt += 1
        else:
            break
    if mx < cnt:
        mx = cnt
        ans = lst

print(mx)
print(*ans)