import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
lst = list(map(int, input().split()))
ans = []
flag = 'F'
for i in range(n-1):
    for j in range(i+1, n):
        if lst[i] < lst[j]:
            ans.append(lst[j])
            flag = 'T'
            break
    if flag == 'F':
        ans.append(-1)

ans.append(-1)
print(*ans)