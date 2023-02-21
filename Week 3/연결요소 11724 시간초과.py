## 문제에 필요없는 부분 없애야
## 방문 표시만 해주면 됨
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

def bfs(start):
    s = start
    q = []
    v = [0] * (n + 1)
    v[s] = 1
    q.append(s)
    alst.append(s)
    while q:
        t = q.pop()
        for e in adj[t]:
            if v[e] == 0:
                v[e] = 1
                alst.append(e)
                q.append(e)