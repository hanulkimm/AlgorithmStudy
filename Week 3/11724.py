import sys
sys.stdin = open('input.txt', 'r')

def dfs(start):
    s = start
    stk = []
    v = [0] * (n + 1)
    v[s] = 1
    alst.append(s)
    while True:
        for e in adj[s]:
            if v[e] == 0:
                stk.append(s)
                s = e
                v[s] = 1
                alst.append(s)
                break
        else:
            if stk:
                s = stk.pop()
            else:
                break


n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
print(adj)
alst = []
cnt = 0
while len(alst) < n:
    for i in range(1,n):
        if i not in alst:
            s = i
    dfs(s)
    cnt += 1
print(cnt)


