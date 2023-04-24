from collections import deque
def bfs(n, cnt):
    global ans
    q = deque()
    q.append((n, cnt))
    while q:
        n, cnt = q.popleft()
        if n==k:
            ans = cnt
            break
        for num in ((n*2, n+1, n-1)):
            if 0<=num<=100000 and v[num]==0:
                v[num]=1
                q.append((num, cnt+1))

n, k = map(int, input().split())
v = [0] * 100001
v[n] = 1
ans = 0
bfs(n, 0)
print(ans)
