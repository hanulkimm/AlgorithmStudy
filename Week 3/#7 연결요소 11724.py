import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10000)

def dfs(s): # 방문 표시해주는 재귀 함수
    v[s] = 1
    for e in adj[s]:
        if not v[e]:
            dfs(e)


n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

v = [0] * (n+1)
cnt = 0
for i in range(1, n+1):
    if not v[i]:
        dfs(i)
        cnt += 1
print(cnt)