lst = list(input())
n = len(lst)
ans = []
i = 0
while i < n:
    if lst[i] == '<':
        for j in range(i+1,n):
            if lst[j] == '>':
                ans.append(lst[i:j+1])
                i = j + 1
                break

    elif lst[i] == ' ':
        ans.append([' '])
        i += 1
    else:
        for j in range(i+1, n):
            if lst[j] == ' ' or lst[j] == '<' or lst[j] == '>':
                ans.append(lst[i:j][::-1])
                i = j
                break
            if j == n-1:
                ans.append(lst[i:j+1][::-1])
                i = n
                break

final = []
for lst in ans:
    for i in lst:
        final.append(i)
print(*final,sep='')
