lst = list(input())
n = len(lst)
ans = []
i = 0
while i < n:
    if lst[i] == '<': # '<'일 때 
        for j in range(i+1,n):
            if lst[j] == '>':
                ans.append(lst[i:j+1])
                i = j + 1
                break

    elif lst[i] == ' ': # 공백일 때 
        ans.append([' '])
        i += 1 
    else: # 문자일 때
        for j in range(i+1, n):
            if lst[j] == ' ' or lst[j] == '<' or lst[j] == '>': # 글자 제외한 것 만났을 때
                ans.append(lst[i:j][::-1])
                i = j
                break
            if j == n-1: # 끝까지 문자일 때
                ans.append(lst[i:j+1][::-1])
                i = n
                break

final = []
for lst in ans:
    for i in lst:
        final.append(i)
print(*final,sep='')
