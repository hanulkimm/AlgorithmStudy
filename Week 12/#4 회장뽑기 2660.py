import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
def bfs(i):
    q = deque()
    q.append((i, 0))
    v[i]=1
    tmp = 0
    while q:
        i, cnt = q.popleft()
        if adj[i]:
            for j in adj[i]:
                if v[j]==0:
                    v[j] = 1
                    q.append((j, cnt+1))
        if tmp<cnt:
            tmp = cnt
    return tmp
n = int(input())
adj = [[] for _ in range(n+1)]
while True:
    a, b = map(int, input().split())
    if a==-1:
        break
    else:
        adj[a].append(b)
        adj[b].append(a)


ans_lst = []
for i in range(1,n+1):
    v = [0] * (n+1)
    total = bfs(i)
    ans_lst.append(total)
print(min(ans_lst), ans_lst.count(min(ans_lst)))
for i in range(len(ans_lst)):
    if ans_lst[i]==min(ans_lst):
        print(i+1, end=' ')