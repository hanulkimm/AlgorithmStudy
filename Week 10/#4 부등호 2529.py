def dfs(cnt, st):
    global mn, mx
    if cnt == k + 1:
        mn = min(int(mn), int(st))
        mx = max(int(mx), int(st))
        return
    if cnt == 0:
        for j in range(10):
            v[j] = 1
            dfs(cnt + 1, st + str(j))
            v[j]=0
    else:
        for j in range(10):
            if v[j] == 0:
                if lst[cnt - 1] == '<':
                    if int(st[cnt - 1]) < j:
                        v[j]=1
                        dfs(cnt + 1, st + str(j))
                        v[j]=0
                elif lst[cnt - 1] == '>':
                    if int(st[cnt - 1]) > j:
                        v[j]=1
                        dfs(cnt + 1, st + str(j))
                        v[j]=0


k = int(input())
lst = list(input().split())
v = [0] * 10
mn, mx = '9' * (k + 1), '0' * (k + 1)
dfs(0, '')  # cnt, st
print(str(mx).zfill(k+1))
print(str(mn).zfill(k+1))

