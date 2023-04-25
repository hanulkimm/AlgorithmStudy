## pypy3 제출
## python 시간초과
from collections import deque
def bfs(computer, time):
    q = deque()
    q.append((computer, time))
    v[computer] = 0
    while q:
        computer, time = q.popleft()
        if adj[computer]:
            for next, t in adj[computer]:
                if v[next]>time+t:
                    v[next] = time+t
                    q.append((next, time+t))

n = int(input())
for _ in range(n):
    n, d, c = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        adj[b].append((a, s))
    INF = 1e9
    v = [INF] * (n+1)
    bfs(c, 0)
    ans_num , ans_time = 0, 0
    for i in range(1, n+1):
        if v[i]<INF:
            ans_num += 1
            ans_time = max(ans_time, v[i])
    print(ans_num, ans_time)
