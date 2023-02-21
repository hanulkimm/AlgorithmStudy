## 시간 초과 ##
# 다른 방법 생각하기..

n = int(input())
lst = list(map(int, input().split()))
ans = []

for i in range(n-1):
    flag = 'F'
    for j in range(i+1, n):
        if lst[i] < lst[j]:
            ans.append(lst[j])
            flag = 'T'
            break
    if flag == 'F':
        ans.append(-1)

ans.append(-1)
print(*ans)